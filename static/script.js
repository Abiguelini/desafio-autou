async function analisar() {
    const texto = document.getElementById('emailTexto').value;
    const btn = document.querySelector('button');
    const loading = document.getElementById('loadingSpinner');
    const resultadoDiv = document.getElementById('resultado');

    if (!texto) {
        alert("Por favor, insira o texto de um email.");
        return;
    }

    // Mostrar loading e esconder resultado anterior
    loading.style.display = 'block';
    resultadoDiv.style.display = 'none';
    btn.disabled = true;

    try {
        const response = await fetch('/analisar', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email_texto: texto })
        });

        if (!response.ok) {
            throw new Error('Erro na rede ou servidor');
        }

        const data = await response.json();

        // Exibir resultados
        const classificacaoEl = document.getElementById('classificacao');
        document.getElementById('sugestao').textContent = data.sugestao_resposta;
        
        classificacaoEl.textContent = data.classificacao;
        // Aplica a classe CSS correta para a "badge"
        classificacaoEl.className = 'badge'; // Limpa classes anteriores
        if (data.classificacao.toLowerCase() === 'produtivo') {
            classificacaoEl.classList.add('produtivo');
        } else {
            classificacaoEl.classList.add('improdutivo');
        }
        
        resultadoDiv.style.display = 'block';

    } catch (error) {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao analisar o email. Tente novamente.');
    } finally {
        // Esconder loading e reabilitar botão
        loading.style.display = 'none';
        btn.disabled = false;
    }
    
}