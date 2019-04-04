var shell = require('shelljs');
var fs = require('fs');
var xlsx = require('node-xlsx');
var fulltextsearchlight = require('full-text-search-light');
var prepos = ["olá", "ola", "oi", "bom", "dia", "boa", "tarde", "noite", "a",
"o", "as", "os", "e", "ao", "aos", "à", "até", "não", "após", "ante", "com",
"conforme", "contra", "de", "da", "do", "desde", "durante", "em", "entre",
"mediante", "para", "perante", "por", "salvo", "sem", "sob", "sobre", "trás",
"antes", "depois"]


class TRLegal {
  constructor(message) {
    this.message = message;
    this.success = false;
    this.answers = [];
    this.source = xlsx.parse('..\\knowledge\\pis-pasesp.xlsx');
    this.qas = this.getQAs();
  }

  // get an array with questions and answers
  getQAs(){
    var qas = [];
    this.source.forEach(function(sheet){
      sheet["data"].forEach(function(row){
        if(row[1] != undefined || row[2] != undefined){
          qas.push([row[1], row[2]]);
        }
      })
    });
    return qas;
  }

  processXL(){
    var search = new fulltextsearchlight( { ignore_case: true } );
    this.qas.forEach(function(qa){
      search.add({ question: qa[0], answer: qa[1]})
    })

    var found_answers = search.search(this.message);

    console.log("Pergunta: " + this.message);
    if (found_answers.length > 0){
      this.answers = found_answers;
      this.success = true;
      console.log("Respostas: " + this.answers.length);
      return true;
    }else{
      console.log("!NOT FOUND!");
      this.success = false;
      return false;
    }

  }
}

module.exports = function(controller) {

  controller.on('message_received', function(bot, message) {
      bot.reply(message, {text: "Humn ... deixe me pensar ...", typing: true });
      legal = new TRLegal();
      legal.message = message.text;
      console.log(legal.message);
      if(legal.processXL()){
        var text = "";
        var replies = [{ title: 'Help', payload: 'help', }];
        if(legal.answers.length > 1){
          text = "Humn ... I did not undertand what you tried to ask. Maybe you tried to ask about the following subjects:"
          legal.answers.forEach(function(a){
            replies.push({title: a['question'], payload: a['question']});
          })
        }else{
          replies.push({ title: 'Entendi', payload: 'finish'});
          replies.push({ title: 'Não me ajudou', payload: 'reset' });
          text = legal.answers[0].answer;
        }

        bot.reply(message, {
          typing: true, text: text, quick_replies: replies
        });
      }else{
        bot.reply(message, {
          text: 'I do not know how to respond to that message yet. [Chat with our support!](https://chatgem.herokuapp.com).',
            quick_replies: replies
        });
      }
  });

}



// processText(){
//   if (shell.exec('python ..\\pythonread\\docreader.py').code !== 0) {
//     shell.echo('Error on trying to process text');
//     shell.exit(1);
//   } else {
//     var contents = fs.readFileSync('pdf.txt', 'utf8');
//     this.answer = contents;
//     var words = ['ronaldo', 'possan', 'c++'];
//     var found = false;
//     var valids = "usuario usuário login logar user account"
//     var query = this.message.split(" ");
//     query.forEach(function (word) {
//       if (valids.includes(word)) {
//         found = true;
//         return;
//       }
//     })
//     this.success = found;
//     console.log(">>>>>>>>>>>>>>>>" + found)
//     shell.echo('BANG!');
//     return this.success;
//   }
// }
