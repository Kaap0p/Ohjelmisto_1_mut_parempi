'use strict';

const names = ['John', 'Paul', 'Jones'];
const target = document.getElementById('target');

if (target) {
  target.classList.add('my-list');
  target.innerHTML = names.map(name => `<li>${name}</li>`).join('');
}