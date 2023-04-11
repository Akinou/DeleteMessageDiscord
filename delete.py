const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Connecté en tant que ${client.user.tag} !`);
});

client.on('message', message => {
  if (message.content === '!supprimer messages') {
    message.channel.messages.fetch({ limit: 100 }).then(messages => {
      messages.forEach(message => {
        if (message.author.id === client.user.id) {
          message.delete();
        }
      });
    });
  }
});

client.login('votre-jeton-ici');
