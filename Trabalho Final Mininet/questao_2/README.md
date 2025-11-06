# Atividade 2

## Propósito da atividade

O texto abaixo descreve o propósito e os requisitos da atividade:

```text
- Com uso de linha de comando padrão do Mininet, crie a
topologia customizada considerando o endereço MAC
padronizado e controlador manual;
- Inspecione informações das interfaces, endereços MAC, IP e
portas através de linhas de comando;
- Crie um desenho ilustrativo da topologia com todas as
informações obtidas no item anterior;
- Faça testes de ping considerando os switches normais;
- Apague as regras anteriores e crie regras baseadas em
endereços MAC para alguns nós. (Deve-se comunicar hosts
dos diferentes switches);
- Faça testes de ping para demonstrar que as regras foram bem 
implementadas
```

Topologia customizada requerida pela atividade

![Topologia customizada](imagens/topologia_custom.png)

## 1 - Código da topologia

O código abaixo abaixo pode ser encontrado nesse projeto. Está localizado em [custom_topo.py](custom_topo.py)

![Custom Topology code](imagens/custom_topo_code.png)

## 2 - Criar a topologia

```bash
sudo mn --custom custom_topo.py --topo customtopo
```

![Creating Custom Topology](imagens/creating_topo.png)

### 3 - Inspeção das interfaces, endereços MAC, IP e portas

#### Listar nós, mostrar a topologia e links e ostrar tabela resumida (hosts, switches, interfaces)

```bash
nodes
net
dump
host/switch ifconfig -a
```

#### Nós da topoliga

## ![Nodes](imagens/nodes.png)

#### Rede da topologia

## ![Net](imagens/net.png)

#### Endereço das portas lógicas

![Dump](imagens/dump.png)

#### Host data

![h1 Data](imagens/h1_data.png)
![h2 Data](imagens/h2_data.png)
![h3 Data](imagens/h3_data.png)
![h4 Data](imagens/h4_data.png)
![h5 Data](imagens/h5_data.png)

### 4 - Desenho ilustrativo da topologia

![Desenho Topologia](imagens/diagrama.jpg)

### 5 - Teste de ping

![Ping](imagens/pings.png)

### 5 - Recriar Regras

#### Deletar regras existentes

![Deleting](imagens/deleted-rules.png)

#### Criar regras para comunicação h1-h4

![New Rules](imagens/uptade_custom_topo.png)

#### Teste de ping para as novas regras

![Ping new rules](imagens/ping_h1-h4.png)
