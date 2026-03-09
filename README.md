# Automação de Monitoramento do Diário Oficial

Projeto em Python para automatizar a busca de editais no Diário Oficial.

## Funcionalidades

- Abertura automática do Diário Oficial
- Busca por palavras-chave específicas
- Captura de tela do resultado
- Envio da notificação via WhatsApp

## Tecnologias

- Python
- Selenium
- PyAutoGUI
- Automação de navegador

## Observação Importante

O envio da mensagem pelo WhatsApp utiliza automação de interface com a biblioteca **PyAutoGUI**.  
Por esse motivo, as **coordenadas da tela utilizadas no código podem variar dependendo da resolução do monitor e da posição da janela**.

Após a abertura do WhatsApp, é necessário **ajustar manualmente as coordenadas do clique na barra de pesquisa** para que o script funcione corretamente no seu computador.

Exemplo no código:

```python
pyautogui.click(x=191, y=122)
```

Esses valores devem ser substituídos pelas coordenadas correspondentes à **barra de pesquisa do WhatsApp na sua tela**.

Uma forma simples de descobrir essas coordenadas é utilizando:

```python
pyautogui.position()
```

ou movendo o mouse até a posição desejada e verificando as coordenadas exibidas pelo PyAutoGUI.
