
const titulo = document.createElement('h1');
titulo.id = 'titulo';
titulo.textContent = 'Welcome to Our Product Page';
document.body.prepend(titulo);

const produto = {
    nome: 'Smartphone XYZ',
    descricao: 'A high-end smartphone with amazing features.',
    preco: 'R$ 3.500,00',
    imagem: 'https://via.placeholder.com/150' 
};

const containerProduto = document.createElement('div');
containerProduto.id = 'produto-container';

const tituloProduto = document.createElement('h2');
tituloProduto.textContent = produto.nome;
containerProduto.appendChild(tituloProduto);

const descricaoProduto = document.createElement('p');
descricaoProduto.textContent = produto.descricao;
containerProduto.appendChild(descricaoProduto);

const precoProduto = document.createElement('p');
precoProduto.textContent = `Price: ${produto.preco}`;
containerProduto.appendChild(precoProduto);

const imagemProduto = document.createElement('img');
imagemProduto.src = produto.imagem;
imagemProduto.alt = produto.nome;
containerProduto.appendChild(imagemProduto);

document.body.appendChild(containerProduto);
