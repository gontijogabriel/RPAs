# Kabum RPA

Este projeto automatiza a coleta de informações de produtos de um site de e-commerce (Kabum) utilizando Selenium. O script permite realizar uma busca com base em um termo fornecido pelo usuário, coleta dados relevantes dos produtos retornados e os armazena em um arquivo CSV.

## Funcionamento do Código

### Resumo

O **Kabum RPA** é um scraper que utiliza selenium que interage diretamente com a página de resultados de produtos no site Kabum. Ele coleta informações como título, preço, URL e imagem dos produtos. Além disso, o script navega automaticamente por múltiplas páginas de resultados, respeitando limites de dados configuráveis. Todos os dados coletados são salvos em um arquivo CSV para posterior análise ou uso.

### Recursos do Projeto Kabum:
- Entrada dinâmica do termo de busca fornecido pelo usuário.
- Extração automática de informações essenciais dos produtos:
  - Título
  - Preço
  - URL do produto
  - Imagem do produto
- Suporte a navegação em múltiplas páginas de resultados (paginação).
- Limitação opcional de quantos dados devem ser coletados.
- Exportação dos dados em um arquivo CSV para facilitar a manipulação e visualização posterior.

### Descrição dos Componentes

1. **Bibliotecas e Módulos Importados**:
   - **Selenium**: Controla o navegador e realiza o scraping, permitindo a interação automática com as páginas da web.
   - **webdriver_manager**: Automatiza a instalação e gerenciamento da versão correta do ChromeDriver, evitando problemas de compatibilidade.
   - **utils.py**: Contém a função `save`, responsável por salvar os dados coletados em um arquivo CSV.

2. **Entrada de Termo de Busca**:
   - O usuário fornece o termo de pesquisa desejado, que é utilizado para gerar a URL de busca no Kabum.

3. **Inicialização do Navegador**:
   - O ChromeDriver é configurado e iniciado. Em seguida, o navegador é direcionado para a URL de busca com base no termo fornecido.

4. **Extração de Dados**:
   - Os dados dos produtos são armazenados em um dicionário `data`, que inclui:
     - Título do produto
     - Preço
     - URL da página do produto
     - URL da imagem do produto
   - A função `scraper()` é responsável pela captura desses dados, utilizando seletores CSS (`CLASS_NAME` e `TAG_NAME`) para localizar os elementos correspondentes a cada produto.

5. **Paginação**:
   - O scraper identifica a presença de múltiplas páginas de resultados e navega automaticamente por cada página, coletando dados até que todas as páginas sejam processadas ou até atingir o limite definido na variável LIMIT_DATA_ROWS

6. **Salvamento dos Dados**:
   - Após a coleta, os dados são exportados para um arquivo CSV, cujo nome é gerado com base no termo de busca inserido pelo usuário.