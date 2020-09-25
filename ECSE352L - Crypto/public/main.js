var ws = new WebSocket('ws://127.0.0.1:5678/');

//defining bootstrap styling classes
let messageContainer = 'list-group-item';
let senderName = 'badge';

const getMessageElement = (msg, sender) => {
	//creating teh current message element
	let message = document.createElement('li');
	//styling
	message.classList.add(messageContainer);

	//adding the tag for sender
	let tag = document.createElement('span');
	//styling
	tag.classList.add(senderName);
	tag.classList.add('badge-primary');
	tag.appendChild(document.createTextNode(sender));

	//adding message content
	content = document.createTextNode(msg);
	message.appendChild(tag);
	message.appendChild(document.createElement('br'));
	message.appendChild(content);

	return message;
};

const addMessageToChatbox = (element) => {
	var chatbox = document.getElementsByTagName('ul')[0];
	chatbox.appendChild(element);

	container = document.getElementById('chatbox');
	container.scroll(0, 999999999);
};

const handler = (event) => {
	data = event.data ? event.data : 'connection refused';
	addMessageToChatbox(getMessageElement(data, 'Server'));
};

ws.onmessage = handler;

ws.onerror = handler;

const sendMessage = () => {
	let inputArea = document.getElementById('message');
	let message = inputArea.value;
	inputArea.value = '';
	addMessageToChatbox(getMessageElement(message, 'Client'));
};

document.getElementById('sendMessage').addEventListener('click', sendMessage);
