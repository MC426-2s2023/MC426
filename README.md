# Repositório para o projeto de MC426
* Na atualidade, diversos problemas no âmbito de segurança pública aparecem em aberto na sociedade.
Nesse contexto, nosso projeto visa a solução de um desses problemas, sendo o principal objetivo construir uma solução de software que use as práticas ensinadas na disciplina.

## Alunos:
* Bruno Sussel Mendes Cunha Bastos - 246992
* Giovanni Machado Quintella Gama  - 247122
* João Víctor dos Santos Oliveira  - 199815
* Paulo Vitor Rodrigues Nogueira   - 247309
* Victor Honório Pereira da Silva  - 247388

## Descrição da Arquitetura:
![A4](https://github.com/MC426-2s2023/MC426/assets/79541075/f12cb2b9-1498-41fa-ba56-17c0ca59c7e3)

* Estilo Arquitetural:
  * O estilo arquitetural adotado é o Model-View-Template (MVT), que é uma variação do padrão Model-View-Controller (MVC) e é o padrão utilizado pelo framework Django. No MVT, o Model representa a estrutura de dados da aplicação, o View corresponde à lógica de negócios, e o Template é a camada de apresentação que lida com a entrega de informação ao cliente. Diferentemente do MVC, onde o controller manipula as requisições, no MVT esse papel é desempenhado pelas views.

* Descrição Textual dos Principais Componentes:
  * Componente de Registro e Autenticação de Usuário: Este componente é responsável pelo gerenciamento de usuários, incluindo registro, autenticação e manutenção de sessões de usuário. Utiliza o sistema de autenticação do Django para garantir a segurança dos dados de acesso dos usuários.

  * Componente de Feedback: Permite que os usuários enviem feedbacks para os desenvolvedores da aplicação. Ele atua como um canal direto entre os usuários e a equipe de desenvolvimento, coletando as respostas no banco de dados.

  * Componente de Registro de Ocorrência: Possibilita que os usuários informem sobre ocorrências de crimes através da aplicação. Esses registros são armazenados no banco de dados e incluem informações geográficas para mapeamento.

  * Componente de Mapas e Rotas: Fornece aos usuários visualizações de mapas de calor da criminalidade e sugere rotas seguras. Utiliza bibliotecas JavaScript externas para apresentação e mapeamento de dados geográficos.

  * Banco de Dados: O coração da aplicação, onde todas as informações coletadas pelos componentes são armazenadas. Segue as práticas de segurança para armazenamento e recuperação de dados.

  * Sistema de Autenticação: Um sistema externo que complementa o componente de registro e autenticação, provendo uma camada adicional de segurança através de criptografia e decodificação de senhas.

  * Sistema de Notificação: Informa os usuários sobre novas ocorrências ou atualizações importantes através do navegador ou dispositivos móveis, mantendo-os informados e engajados com a aplicação.

  * Sistema de Mapeamento e Rotas: Integra-se com o componente de mapas e rotas para fornecer visualizações interativas e cálculo de rotas através de serviços de mapeamento externos.
