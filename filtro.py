import requests

sites_acessiveis = []

# Leitura do arquivo com os sites
with open('list_browser.txt', 'r') as file:
    sites = file.readlines()

for site in sites:
    url = site.strip()  # Remove espaços em branco ou caracteres de nova linha

    try:
        response = requests.get(url)
        if response.status_code == 200:
            sites_acessiveis.append(url)
            print(f'O site {url} está acessível.')
        else:
            print(f'O site {url} não está acessível. Código de status: {response.status_code}')
    except requests.RequestException as e:
        print(f'O site {url} não está acessível. Erro: {e}')

with open('sites_acessiveis.txt', 'w') as output_file:
    for site in sites_acessiveis:
        output_file.write(site + '\n')

print("Lista de sites acessíveis salva em sites_acessiveis.txt")
