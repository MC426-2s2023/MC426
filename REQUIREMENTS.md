# Técnica de elicitação: Benchmarking
Para esta etapa do projeto, o grupo dividiu as features definidas até então entre os cinco integrantes: 
Login-Giovanni, Heatmap-João Víctor, Feedback-Victor, Registro de ocorrências-Bruno e notificação-Paulo Vitor.

Cada integrante registrou as evidências por meio de vídeos e/ou textos, demonstrando outras aplicações que compartilham da funcionalidade em questão.

Segue link para acessar o drive com as evidências
* https://drive.google.com/drive/folders/1bJlEeLaPoEzBCxCrUVzwvw5jqNHHD6LU

# 1: HeatMap
[Video 1.1](https://drive.google.com/file/d/19_aA-uO1YjUHdsJMPGUnQoFTjsvUn03G/view?usp=drive_link)

[Video 1.2](https://drive.google.com/file/d/1B51rN0roNljR8oCuMdpJlkEs9C4Vqdlp/view?usp=drive_link)

# 2: Login
[Video 2.1](https://drive.google.com/file/d/1y2tmo81f4ZNa_SKpYZ9oThJM3A1x5IIr/view?usp=drive_link)

[Video 2.2](https://drive.google.com/file/d/1JkYq_ncAUWZWT2EhHLGVWw2sgmR62DrU/view?usp=drive_link)

# 3: Registro de ocorrências

Waze: escolhido pela funcionalidade de envio e visualização de alertas dados pelos usuários desse sistema. Um sistema desse tipo pode ser implementado para atualizar o mapa de calor.

## Funcionalidades
- Funcionalidade de alertas de usuários: pode-se enviar um alerta no mapa, ligado à localização atual do usuário no mapa, sobre vários eventos relacionados ao trânsito, tais como condição de tráfego, obras, polícia, objetos na via/acostamento, etc. Esses alertas podem ser vistos por outros usuários no mapa.

  - Os alertas só podem ser dados por usuários cadastrados que estão no local do evento. No caso do projeto em desenvolvimento, provavelmente deve-se permitir que o usuário envie um alerta depois, em outro lugar. Por exemplo, no caso de ele mesmo ter seu smartphone roubado, é impossível (e perigoso) que ele envie o alerta na hora.
 
  - Alertas relacionados a segurança públicas possíveis: polícia, assaltos (ou outros crimes), vias não iluminadas, ...
 
  - Alertas de assalto (ou outros crimes) podem atualizar o mapa de calor, assim como vias não iluminadas.

- Funcionalidade de comentários: ao enviar um alerta, é possível dar mais detalhes sobre o alerta por meio de um texto e de uma foto. Para alertas de outros usuários, é possível adicionar comentários sobre a situação

  - É possível dar "joinha" nos alertas de outros usuários, o que aumenta a confiabilidade do alerta
  - É possível relatar que o evento do alerta não existe mais
     - Talvez isso seja útil para eventos que podem ser verificados que não existem mais, como patrulhamentos ou falta de iluminação, mas nem tanto para relatos de assalto, que não podem ser verificados por outras pessoas.

- Talvez isso seja útil para eventos que podem ser verificados que não existem mais, como patrulhamentos ou falta de iluminação, mas nem tanto para relatos de assalto, que não podem ser verificados por outras pessoas.
  - Isso pode ser feito no projeto, trocando ocorrência de acidentes de trânsito por assaltos e outros crimes.

## Descrição de funcionamento das funcionalidades citadas:

- Funcionalidade de alerta: (aqui é mostrado o exemplo de alertar sobre engarrafamentos, disponível em https://support.google.com/waze/answer/13740207?hl=pt-BR&ref_topic=14098147&sjid=11949782402734955539-SA. Informações sobre outros alertas estão em https://support.google.com/waze/topic/14098147?hl=pt-BR&ref_topic=14113115&sjid=11949782402734955539-SA.)

Alertar sobre engarrafamentos

Informe ao Waze sobre engarrafamentos no seu trajeto para melhorar as rotas traçadas nessa área.

Toque em [botão de envio de alertas].
	Toque em Trânsito.
	Na nova tela aberta, a opção Engarrafamento fica selecionada por padrão para você economizar tempo. Se quiser dar mais detalhes, selecione o nível de gravidade:
    	Intenso
    	Parado
	Toque em Alertar ou aguarde alguns segundos para que o Waze envie seu alerta de forma automática.

Dúvidas?

Como faço para ter certeza de que meu alerta foi adicionado ao mapa?
Só envie alertas sobre incidentes que você presenciar em tempo real e o mais próximo possível deles.

Como remover um alerta errado?
Os alertas aparecem no mapa por um determinado período, dependendo do número de Wazers que reagem a eles.
Se você identificar um alerta que não é mais relevante, toque em Não existe. Isso vai fazer com que ele desapareça logo do app.

E se eu perder a conexão de Internet durante um alerta?
O Waze salva e envia o alerta automaticamente quando você se reconecta à rede.

O que são alertas em excesso e como posso evitar isso?
O Waze limita a quantidade de vezes que um usuário pode enviar alertas para reduzir as chances de spam e relatos incorretos. Os usuários com suspeita de excesso de alertas podem ser impedidos de enviar essas informações no mapa. Limite seus alertas a uma vez por minuto para evitar esse problema.

Outros usuários terão acesso ao meu nome de usuário?
Sim. Seu nome de usuário aparece no alerta adicionado ao mapa e fica visível para outras pessoas.

- Funcionalidade de aviso de via com alto índice de acidentes (disponível em https://support.google.com/waze/answer/13014546?hl=pt-BR&ref_topic=7060192&sjid=11949782402734955539-SA.)

Receber alertas sobre vias com histórico de acidentes

Com base no seu trajeto e nas informações enviadas por motoristas, o Waze mostra alertas de "Histórico de acidentes". Esses avisos são dinâmicos e consideram o trânsito atual, as condições da via, o dia da semana, o horário do dia e o histórico mais recente de acidentes reportados.

Você só recebe alertas nos locais e momentos mais importantes. Por exemplo:

- Talvez os avisos não apareçam para vias em que você dirige com frequência.

- Se o trajeto tiver várias vias com histórico de acidentes, o Waze vai alertar apenas sobre as mais perigosas.

- Pode aparecer um alerta para várias vias afetadas na mesma área.

Observações:

- O histórico de acidentes se baseia nas informações enviadas pelos usuários. Se um acidente não foi reportado, o Waze não tem conhecimento dele.

- Se um alerta não aparecer, isso não significa necessariamente que uma via não tem histórico de acidentes.

- Os avisos não fazem distinção entre acidentes leves e graves.

Desativar alertas

	Abra o Waze.
 	Toque em [ícone de menu].
	Toque em Configurações.
	Vá para Alertas e relatórios e, depois, Relatórios.
	Toque em [ícone de “Histórico de acidentes”].
	Desative a opção Alertar enquanto dirige.

Há também uma matéria sobre o tema em: https://www.uol.com.br/tilt/noticias/redacao/2023/11/07/waze-vai-dedurar-para-motoristas-as-vias-com-historico-de-acidentes.htm.

Capturas de tela com a funcionalidade de envio de alertas e comentários:

<img src="https://github.com/MC426-2s2023/MC426/assets/142899966/29595d7a-8983-4320-989a-6a3c7ba1c409" width=50% height=50%>

Tela inicial, com o botão laranja no canto inferior direito sendo o botão de enviar alertas
(o mapa foi borrado para não revelar localização)

<img src="https://github.com/MC426-2s2023/MC426/assets/142899966/a18ef1b7-9efd-4113-9287-3b20a53ef331" width=50% height=50%>

Tela de seleção de tipo de alerta a ser enviado

<img src="https://github.com/MC426-2s2023/MC426/assets/142899966/e59207e1-aed1-4eae-9ce8-d63fc3e0cc77" width=50% height=50%>

Tela de especificação do alerta. Note a possibilidade de tirar foto e comentar.

<img src="https://github.com/MC426-2s2023/MC426/assets/142899966/42b2014b-39a9-460b-b9cb-96e83d18c5d0" width=50% height=50%>

Tela para mais especificações ainda do alerta.

<img src="https://github.com/MC426-2s2023/MC426/assets/142899966/819a37bc-fb10-4b5f-a6ab-4ac1b125304c" width=50% height=50%>

Tela de envio de comentário do usuário que envia o alerta.

<img src="https://github.com/MC426-2s2023/MC426/assets/142899966/87515d9b-aaf0-4fc9-b7d9-85569ba26272" width=50% height=50%>

Visualização de vários alertas (alertas com comentário têm ícone de “balãozinho” verde próximo a eles)

<img src="https://github.com/MC426-2s2023/MC426/assets/142899966/26d8b071-d5da-4715-ab3a-d5152e5842c6" width=50% height=50%>

Tela de visualização de alerta. Note o botão de comentar e de “joinha”.

<img src="https://github.com/MC426-2s2023/MC426/assets/142899966/77cbb689-8aac-43b5-85fb-6c8c55678630" width=50% height=50%>

Tela de comentários de um alerta.

<img src="https://github.com/MC426-2s2023/MC426/assets/142899966/ea6a8c34-d6e3-4c8e-8a32-f658e482ebec" width=50% height=50%>

Tela de alerta com comentário dado pelo usuário que o enviou. No caso, o comentário é “Obras de implantação das marginais da rodovia”.

- Pontos positivos:
  - Participação ativa de usuários melhora o sistema, e pode incentivar os usuários a utilizarem o serviço

- Pontos negativos:
  - Possibilidade de marcação de eventos falsos, ou da inexistência de eventos verdadeiros
  - Possibilidade de envio de comentários pouco úteis.
  - Pode incentivar uso de smartphone no trânsito, o que aumenta riscos (No caso do nosso projeto, a utilização de smartphone em situações de risco de segurança também não é boa)
  - Patrulhamento policial pode ser afetado se houver aviso

# 4 - Feedback


[Video 4.1](https://drive.google.com/file/d/1fe98RWcPnrIC0lsDE7daJPrnGXv6pAXT/view?usp=drive_link)

[Video 4.2](https://drive.google.com/file/d/11Vw2Gs8-VGjCeOPmCuej90YuVkzLZXnO/view?usp=drive_link)

[Video 4.3](https://drive.google.com/file/d/1oMxbcC1kc44EKN4HNa2znq3rAwYLQFMV/view?usp=drive_link)

## Análise da Funcionalidade do Feedback em algumas aplicações

### Site SpotCrime: 
Escolhido por se aproximar do objetivo do projeto de mapear áreas de acordo com a ocorrência de crimes e alertar os usuários sobre eventos recentes. 

Com relação à funcionalidade de feedback, no site SpotCrime é possível perceber um sistema simples de feedback, em que o usuário indica o seu email e submete a sua mensagem para a equipe retornar assim que possível. O ponto positivo dessa aplicação está na praticidade e na facilidade de se enviar um feedback: por haver apenas uma forma de envio, qualquer usuário poderá enviar da mesma forma, sem precisar entregar muitas informações sobre si. O ponto negativo está no detalhamento da informação: por se tratar de uma aba simples de mensagem e uma de e-mail, não existem garantias de que o usuário colocará todas as informações necessárias para o entendimento do ocorrido.

![Pasted image](https://github.com/MC426-2s2023/MC426/assets/142899966/3222fedd-3407-4b82-8e19-fb172bc78315)

![Pasted image 1](https://github.com/MC426-2s2023/MC426/assets/142899966/e469a530-92f6-4ca0-a188-4ba3ae059ad6)

### Site CrimeMapping.com
No site CrimeMapping, percebemos um sistema parecido com o sistema anterior, porém com um pouco mais de informações para serem inseridas. Nesse sistema, é possível escolher entre dois caminhos, tanto para suporte geral, como também para compras. Ou seja, é possível detalhar melhor o tipo de usuário que será responsável por reportar a informação. Um aspecto positivo extra está na melhor divisão entre usuários, uma focada no usuário normal e outra focada em prestadores de serviços. Como aspecto negativo, porém, ainda está na ausência de um detalhamento maior do tipo de feedback a ser enviado, o que pode gerar uma dificuldade nos receptores do feedback de filtrar a informação por tipo: uma denúncia, uma dúvida, uma sugestão.

![Pasted image 2](https://github.com/MC426-2s2023/MC426/assets/142899966/861f7ab3-5f8d-4fb5-bfe7-b9803216bb8b)

![Pasted image 3](https://github.com/MC426-2s2023/MC426/assets/142899966/d84027b4-9c5e-4a61-ab8c-f589edbc6d2b)

![Pasted image 4](https://github.com/MC426-2s2023/MC426/assets/142899966/b2085815-c219-498b-9e78-b3aec8ddb3b1)

### Site Minneapolismn.gov
O site Minneapolismn.gov apresenta informações gerais sobre a cidade, serviços em geral que possam ser úteis à população. Na área de feedback, podemos destacar uma interface de reporte de problemas, bem dividida por áreas, por exemplo: problemas de propriedade e na vizinhança, problemas de utilidade, de tráfego, e na nossa área especificamente, problemas de segurança pública.
Ao verificar o setor de problemas de segurança pública, percebe-se o detalhamento do site, com abas para todos os problemas gerais bem definidos. Clicando em um problema em específico, no caso, abandono de veículo, temos um redirecionamento para uma página norteando o usuário a como proceder para reportar a informação da melhor forma. Outros problemas podem redirecionar o usuário a uma aba de especialistas. Desse modo, percebe-se como aspecto muito positivo o detalhamento preciso de informações possíveis de serem procuradas, mostrando o exato caminho a ser percorrido e a quem recorrer também. Porém, como aspecto negativo, temos uma perda de simplicidade na mensagem rápida, sendo necessário procurar qual é a situação específica à qual você deseja se comunicar sobre. Seria interessante não deixar de apresentar uma aba de dúvidas simples para serem enviadas, visto que muitos usuários poderiam ficar confusos em virtude da grande quantidade de informações presentes na aplicação.

![Pasted image 5](https://github.com/MC426-2s2023/MC426/assets/142899966/e0e294d7-d4d9-44f8-886c-21a18c689de4)

![image](https://github.com/MC426-2s2023/MC426/assets/142899966/7d019622-e0ab-4eed-83c3-fae4dc09a828)

![Pasted image 7](https://github.com/MC426-2s2023/MC426/assets/142899966/9b7c98e7-7a5c-4b97-9c19-bfd0e78dbbba)

![Pasted image 8](https://github.com/MC426-2s2023/MC426/assets/142899966/e08a333b-b78d-48db-b91c-b6f564b1b16e)

# 5 - Notificação

## Funcionalidade de interesse: enviar mensagens atualizando o usuário através de notificações push.

-  Avisar o usuário quando estiver na proximidade de uma área perigosa ou com registro de ocorrências criminais recentemente.
-  Notificar o usuário a respeito do status de seu perfil ou de informações da aplicação.
-  Avisar o usuário a respeito de ocorrências na sua região e sobre quais locais são considerados mais ou menos perigosos.

As funcionalidades citadas acima podem ser implementadas através de notificações push

- Exemplo de funcionamento usando um site que testa push notifications:

  [Video 5.1](https://drive.google.com/file/d/1flwN2wxX8Y9-hgF-Yshk1rKTd44nsxP6/view?usp=drive_link)

  Site: https://cleverpush.com/en/test-notifications/ 

- Exemplo do uso de notificações push em sites de notícias para atualizar o usuário:

  [Video 5.2](https://drive.google.com/file/d/1a5uWFW3Sm53jtxfJxAWxNLldSVjFiWRN/view?usp=drive_link)

  Site: https://www.cnnbrasil.com.br/ 

- Pontos positivos observados:
  - Não dependem do dispositivo, a feature é funcional contanto que o dispositivo usado
implemente push notifications, assim é possível utilizar o mesmo código o uso tanto em dispositivos mobile quanto em desktop.

    - Notificação emitida através do linux usando o gnome como ambiente de desktop:
      
      ![5 1](https://github.com/MC426-2s2023/MC426/assets/142899966/fc218e58-fe5c-4459-a023-15d7d3c83f40)

    - Notificação emitida através do Android:
      
      ![5 2](https://github.com/MC426-2s2023/MC426/assets/142899966/7b1c6aed-1d67-411d-a972-a9d1ac441b0b)

  - Uso de elementos visuais para atrair a atenção do usuário. Ex:
  ![5 3](https://github.com/MC426-2s2023/MC426/assets/142899966/dcc83a5f-5034-467d-87ae-871a7c70cc6d)

    No contexto da aplicação é essencial que alertas de possíveis incidentes criminosos sejam chamativos o bastante para atrair a atenção do usuário com o objetivo de alertá-lo.

- Pontos negativos observados:
  - Requer que o navegador do usuário tenha suporte às notificações.
  - Requer que o usuário ative as notificações.
  - O processo pode ser afetado por configurações de privacidade e permissões no dispositivo.

