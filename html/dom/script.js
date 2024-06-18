const titulo = document.getElementById('titulo');
const ul = document.querySelector('ul');
const a = document.querySelector('a');
const listaOrdenada = document.getElementById('lista-ordenada');


titulo.innerText = 'Bem-vindo ao meu projeto!';
a.innerText = 'Acesse Prozeducação';

ul.innerHTML = `
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
`;

listaOrdenada.innerHTML = `
    <li><a href="https://www.google.com">Google</a></li>
    <li><a href="https://www.facebook.com">Facebook</a></li>
    <li><a href="https://www.twitter.com">Twitter</a></li>
`;
