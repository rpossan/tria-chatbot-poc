var shell = require('shelljs');
var fs = require('fs');

class TRManual {
  constructor(message) {
    this.message = message;
    this.success = false;
    this.answer = "";
  }
  
  processText(){
    if (shell.exec('python ..\\pythonread\\docreader.py').code !== 0) {
      shell.echo('Error on trying to process text');
      shell.exit(1);
    } else{
      var contents = fs.readFileSync('pdf.txt', 'utf8');
      this.answer = contents;
      var words = ['ronaldo','possan', 'c++'];
      var found = false;
      var valids = "usuario usuário login logar user account"
      var query = this.message.split(" ");
      query.forEach(function(word){
        if(valids.includes(word)){
          found = true;
          return;
        }
      })
      
      this.success = found;
      console.log(">>>>>>>>>>>>>>>>" + found)
      shell.echo('BANG!');
      return this.success;
    }
  }
}

module.exports = function(controller) {

  controller.on('message_received', function(bot, message) {

      p = new TRManual();
      p.message = message.text;
      console.log(p.message);
      if(p.processText()){
        bot.reply(message, {
          text: p.answer, quick_replies: [{ title: 'Help', payload: 'help', }, ]
        });
      }else{
        bot.reply(message, {
          text: 'I do not know how to respond to that message yet. [Chat with our support!](https://chatgem.herokuapp.com).',
            quick_replies: [{ title: 'Help', payload: 'help', }, ]
        });
      }
  });

}
