const mp = new MercadoPago('TEST-0b6909dd-8d13-4f55-add2-33387fbf9ce8', {
    locale: 'pt-BR'
});
const csrfmiddlewaretoken = document.querySelector('input[name=csrfmiddlewaretoken]').value
const productName = document.querySelector('input[id=checkout__productName]').value
const productId = document.querySelector('input[id=checkout__productId]').value
const amount = parseFloat(document.getElementById('checkout__productValue').value).toFixed(2)
const bricksBuilder = mp.bricks();

const item = [{
    id: productId,
    title: productName,
}]

// csrfmiddlewaretoken: csrfmiddlewaretoken,

const renderCardPaymentBrick = async (bricksBuilder) => {

    const settings = {
        initialization: {
            amount: amount, // valor total a ser pago
            payer: {
                email: "",
            },
        },
        customization: {
            paymentMethods: {
                maxInstallments: 12,
            },
            items: [
                {
                    id: productId,
                    title: productName,
                    currency_id: "BRL",
                    description: "Descripción del Item",
                    category_id: "art",
                    quantity: 1,
                    unit_price: amount
                }
            ],
            back_urls: {
                "success": "http://localhost:8000/admin/tags",
                "failure": "http://localhost:8000/admin/tags",
                "pending": "http://localhost:8000/admin/tags"
            },
            auto_return: "approved",
            additional_info: item,
            visual: {
                style: {
                    theme: 'default',
                    customVariables: {
                        formBackgroundColor: '##eedaf0',
                        // baseColor: 'aquamarine',
                    },
                    texts: {
                        formTitle: productName
                    },
                }
            }
        },
        callbacks: {
            onReady: () => {
                // callback chamado quando o Brick estiver pronto
            },
            onSubmit: (cardFormData) => {
                let post_service = {
                    product_id: productId,
                    csrfmiddlewaretoken: csrfmiddlewaretoken,
                };
                let body = {
                    cardFormData: cardFormData,
                    post_service: post_service,
                };
                //  callback chamado o usuário clicar no botão de submissão dos dados
                //  exemplo de envio dos dados coletados pelo Brick para seu servidor
                return new Promise((resolve, reject) => {
                    fetch("/process_payment", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                            "X-CSRFToken": csrfmiddlewaretoken
                        },
                        body: JSON.stringify(body)
                    })
                        .then((response) => response.json()) //2
                        .then((id) => {
                            id_payment = String(Object.values(id))
                            url = '/payment?id_payment='+id_payment
                            location.replace(url)
                            resolve();
                        })
                        .catch((error) => {
                            // lidar com a resposta de erro ao tentar criar o pagamento
                            reject();
                        })
                });
            },
            onError: (error) => {
                // callback chamado para todos os casos de erro do Brick
            },
        },
        customization: {
            backUrls: {
                'error': 'http://127.0.0.1/error',
                'return': 'https://google.com/'
            }
        }
    };
    window.cardPaymentBrickController = await bricksBuilder.create('cardPayment', 'cardPaymentBrick_container', settings);
};
renderCardPaymentBrick(bricksBuilder);