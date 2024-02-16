// script pra o Acordeon da FAQ
document.addEventListener("DOMContentLoaded", function () {
	const faqQuestions = document.querySelectorAll(".faq-question");

	faqQuestions.forEach(function (question) {
		question.addEventListener("click", function () {
			const answer = this.nextElementSibling;

			if (answer.style.display === "block") {
				answer.style.display = "none";
				this.classList.remove("open");
			} else {
				answer.style.display = "block";
				this.classList.add("open");
			}
		});
	});
});

// script da alternância dos planos anual e mensal
document.addEventListener('DOMContentLoaded', function () {
	const btnAnual = document.getElementById('btn-anual');
	const btnMensal = document.getElementById('btn-mensal');
	const planoAnualDiv = document.querySelector('.plano-anual');
	const planoMensalDiv = document.querySelector('.plano-mensal');

	btnAnual.addEventListener('click', function () {
		btnAnual.classList.add('selected');
		btnMensal.classList.remove('selected');
		planoAnualDiv.style.display = 'flex';
		planoMensalDiv.style.display = 'none';
	});

	btnMensal.addEventListener('click', function () {
		btnMensal.classList.add('selected');
		btnAnual.classList.remove('selected');
		planoAnualDiv.style.display = 'none';
		planoMensalDiv.style.display = 'flex';
	});

	btnAnual.click(); // Por padrão, exibe os planos anuais
});





document.getElementById('id_phone').addEventListener('input', function (e) {
	var x = e.target.value.replace(/\D/g, '').match(/(\d{0,2})(\d{0,5})(\d{0,4})/);
	e.target.value = !x[2] ? x[1] : '(' + x[1] + ') ' + x[2] + (x[3] ? '-' + x[3] : '');
});

// Implementação do envio ajax do formulario
document.getElementById('lead').addEventListener('submit', function (event) {
	// Impedir o envio padrão do formulário
	event.preventDefault();

	// Obter os dados do formulário
	var formData = new FormData(this);

	// Criar uma instância do objeto XMLHttpRequest
	var xhr = new XMLHttpRequest();

	// Configurar a requisição
	xhr.open('POST', '/send_lead', true);

	// Configurar a função de retorno de chamada
	xhr.onload = function () {
		if (xhr.status == 202) {
			// Sucesso na requisição
			document.getElementById('submitted').textContent = 'Formulário enviado com sucesso!';
			document.getElementById('submitted').classList.add('submitted');
		} else if (xhr.status == 409) {
			// Erro na requisição
			document.getElementById('email').textContent = 'Email já cadastrado, tente um novo email';
			// document.getElementById('submitted').classList.add('submitted');
		} else if (xhr.status == 400) {
			document.getElementById('phone').textContent = 'Numero de telefone inválido';
		} else {
			console.error('Erro ao enviar o formulário. Código do status:', xhr.status);
			document.getElementById('submitted').textContent = 'Erro ao enviar o formulário. Por favor, tente novamente.';
			document.getElementById('submitted').classList.add('submitted');
		}
	};

	// Configurar a função de tratamento de erro
	xhr.onerror = function () {
		console.error('Erro de rede ao enviar o formulário.');
		document.getElementById('submitted').textContent = 'Erro de rede ao enviar o formulário. Por favor, verifique sua conexão e tente novamente.';
	};

	window.onload = function () {
		hideOptionPhoto();
	};

	// Enviar a requisição com os dados do formulário
	xhr.send(formData);
});

