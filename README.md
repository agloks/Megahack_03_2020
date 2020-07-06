<h1 align="center">
	MeuGarçom - Back Repo 
</h1>
<h3 align="center" font-style="italic">
	Sobre o Projeto
</h3>
<p>
A solução “Meu Garçom” é uma inovação incremental que oferece diversas funcionalidades para atrair o consumidor, aumentar o ticket médio da venda, oferecer conveniência, esclarecer menus e ingredientes e fidelizar clientes. Sem contar os demais benefícios de eficiência operacional para a retaguarda e ponto de venda do negócio. Garantindo acima de tudo uma maior segurança em efetuar seu pedido sem necessidade física de um garçom e comodidade ao permitir que o cliente faça seu pedido pelo WhatsApp, sem a necessidade de usar mais um app. Para os empreendedores as vantagens oferecidas são um maior controle e gestão de seus negócios com ganhos em eficiência operacional e diminuição de custos, através de uma solução que fornecerá uma base de dados com maior assertividade sobre os hábitos e costumes de seus clientes. O desafio dos operadores de restaurantes vai além de entender as funcionalidades da tecnologia digital e seus benefícios, mas também de integrar os diferentes canais digitais para que a experiência de seu público seja consistente e complementar entre os diversos pontos de contato digital e físico. O conceito de Omnichannel tem como objetivo integrar os canais digitais para que a proposição de valor da marca seja percebida de forma consistente e complementar pelos clientes. A sinergia dos diversos canais integrados pode criar diferenciação e singularidade para a marca.
</p>
<h3 align="center" font-style="italic">
	Tecnologias Core Do Projeto
</h3>
<p align="center" font-style="cursive">
	 Python | Zenvia API | Google API | Atlas | Flask | IBM Cloud | Heroku | MongoDB
</p>
<h3 align="center" font-style="italic">
	Estrutura Do Projeto
</h3>

```
├── app.py (Bootstrap aplicação)
├── LICENSE
├── manifest.yml (Cloud config)
├── Procfile (Cloud config)
├── README.md
├── requirements.txt 
├── settings_env.py (Cloud config)
├── setup.py (Cloud config)
├── src
│   ├── db (Módulo para a manipulação com o banco de dados)
│   │   ├── connection.py
│   │   ├── DI.py
│   │   ├── model.py
│   │   └── schema_enum.py
│   ├── maps (Módulo para a manipulação com o GOOGLE API)
│   │   ├── DI.py
│   │   ├── doc
│   │   │   ├── documenation_maps.txt
│   │   │   ├── geocoding_response.json
│   │   │   └── place_nearby_response.json
│   │   ├── geocoding.py
│   ├── payment
│   ├── qrcode (Módulo para fazer a geração dos qrcode)
│   │   ├── generator_qrcode.py
│   │   └── imgs
│   │       ├── qrcode_test_eufraten.png
│   │       └── qrcode_test_eufraten.svg
│   ├── utility (Módulo de proposta genéricas com funções de atendimento genérico)
│   │   ├── handlerJson.py
│   │   ├── logger.py
│   └── whataspp (Módulo para a manipulação com o ZENVIA API e responsável pela regra de negócio do chatbot)
│       ├── DI.py
│       ├── doc
│       │   └── response_in.json
│       ├── handler_conversation.py
│       ├── mockup_conversation.py
│       └── whastapp_api.py
├── temp (Pasta para estratégia de cache)
│   ├── 551195069324.json
│   └── test.json
└── vcap-local.template.json (Cloud config)
```

<h3 align="center" font-style="italic">
	Estrutura Do Projeto
</h3>

# Features:

- [x] Resesta conversa após certo tempo sem receber conversa
- [x] Controle de fluxo da conversa para não usar comandos sem está na interação correta
- [x] Ajuda customizada para cada interação
- [x] Cacheamento do nível da interação
- [x] Buscar os estabelecimentos alimenticios mais próximos do endereço
- [x] Geração de qrcode
- [x] Aplicação back servida em difentes clouds caminhando para uma solução em micro serviço
- [x] Desenho do BD e do workflow da aplicação  

# TODO:

- [ ] Servir cardápios
- [ ] Relação de consulta ao banco na interação com chatbot
- [ ] Testes e integração CI/CD
