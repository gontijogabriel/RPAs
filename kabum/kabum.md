# Kabum RPA

Este projeto automatiza a coleta de informações de produtos de um site de e-commerce (Kabum) utilizando Selenium. O script permite realizar uma busca com base em um termo fornecido pelo usuário, coleta dados relevantes dos produtos retornados e os armazena em um arquivo CSV.

## Funcionamento do Código

### Resumo

O **Kabum RPA** é um scraper que interage diretamente com a página de resultados de produtos no site Kabum, utilizando Selenium. Ele coleta informações como título, preço, URL e imagem dos produtos. Além disso, o script navega automaticamente por múltiplas páginas de resultados, respeitando limites de dados configuráveis. Todos os dados coletados são salvos em um arquivo CSV para posterior análise ou uso.

### Recursos do Projeto Kabum:
- Entrada dinâmica do termo de busca fornecido pelo usuário.
- Extração automática de informações essenciais dos produtos:
  - Título
  - Preço
  - URL do produto
  - Imagem do produto.
- Suporte a navegação em múltiplas páginas de resultados (paginação).
- Limitação opcional da quantidade de dados a serem coletados.
- Exportação dos dados em um arquivo CSV para facilitar a manipulação e visualização posterior.

### Descrição dos Componentes

2. **Classe Kabum**:
   - A classe `Kabum` é responsável pela estrutura principal do scraper:
     - **`__init__`**: Inicializa o scraper com o termo de busca, cria a URL da pesquisa e configura o navegador.
     - **`scraper()`**: Coleta informações dos produtos, como título, preço, imagem e URL, e as armazena em um dicionário.
     - **`save()`**: Salva os dados coletados em um arquivo CSV dentro de uma pasta específica.
     - **`run()`**: Gerencia a navegação pelas páginas e controla o fluxo do processo de scraping.

3. **Spinner de Carregamento**:
   - Uma animação simples de carregamento (spinner) é exibida no console enquanto o scraping está sendo realizado, utilizando `threading` para não bloquear a execução principal.

4. **Execução do Script**:
   - O usuário fornece o termo de pesquisa, o scraper é executado e os dados são salvos em um arquivo CSV no diretório `kabum/data`. Caso o diretório não exista, ele é criado automaticamente.

### Como Executar

```bash
python kabum.py
```

### Estrutura do CSV

O arquivo CSV gerado terá o seguinte formato:
- **Título**: Nome do produto.
- **Preço**: Preço do produto.
- **URL da Imagem**: Link da imagem do produto.
- **URL do Produto**: Link da página do produto no Kabum.

### Observações

- O script é projetado para lidar com páginas que contêm múltiplos produtos e pode ser ajustado para diferentes limites de coleta de dados, se necessário.
- Certifique-se de ter o Google Chrome instalado e compatível com a versão do ChromeDriver gerenciado automaticamente pela biblioteca `webdriver-manager`.