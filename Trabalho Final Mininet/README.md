# Trabalho Final Mininet

## Diego Nogueira Rezende Vilela<br> Sabrina Ramos Silveira

### Questão 1

Considere uma topologia arvore com profundidade três e ramificação cinco

- Com uso de linha de comando padrão do Mininet, crie a topologia considerando o endereço MAC padronizado, larguras debanda bw de 30 Mbps e controlador do Mininet (não precisa especificar);
- Inspecione informações das interfaces, endereços MAC, IP e portas através de linhas de comando; 
- Crie um desenho ilustrativo da topologia com todas as informações obtidas no item anterior; 
- Execute testes de ping entre os diferentes nós, mostre os pacotes chegando nos nós com uso do comando tcpdump;
-  Especifique que o host 1 na porta 5555 vai ser um servidor TCP e o host 2 um cliente e execute testes de iperf,considere um relatório por segundo com teste de  20 segundos. Faça os testes para larguras de banda bw de 30 e 40 Mbps(Necessário reconstruir a topologia para os outros valores).

### 1. Criação da topoligia

```bash
sudo mn --topo tree,depth=3,fanout=5 --link tc,bw=30 --mac
```
![alt text](Imagens/1.png)
![alt text](Imagens/2.png)
![alt text](Imagens/3.png)

### 2. Inspeção das interfaces, endereços MAC, IP e portas

#### Listar nós, mostrar a topologia e links e ostrar tabela resumida (hosts, switches, interfaces)

```bash
nodes
```
![alt text](Imagens/4.png)

```bash
net
```
![alt text](Imagens/5.png)
![alt text](Imagens/6.png)
![alt text](Imagens/7.png)
![alt text](Imagens/8.png)

```bash
dump
```
![alt text](Imagens/9.png)
![alt text](Imagens/10.png)
![alt text](Imagens/11.png)
![alt text](Imagens/12.png)

#### Inspecionar endereços (h1 - h125, mas print até h10)

```bash
h1 ifconfig
```
![alt text](Imagens/13.png)

```bash
h2 ifconfig
```
![alt text](Imagens/14.png)

```bash
h3 ifconfig
```
![alt text](Imagens/15.png)

```bash
h4 ifconfig
```
![alt text](Imagens/16.png)

```bash
h5 ifconfig
```
![alt text](Imagens/17.png)

```bash
h6 ifconfig
```
![alt text](Imagens/18.png)

```bash
h7 ifconfig
```
![alt text](Imagens/19.png)

```bash
h8 ifconfig
```
![alt text](Imagens/20.png)

```bash
h9 ifconfig
```
![alt text](Imagens/21.png)

```bash
h10 ifconfig
```
![alt text](Imagens/22.png)

#### Inspecionar switch (todos verificados mas print apenas de s1)

```bash
s1 ifconfig
```
![alt text](Imagens/23.png)
[Visualizar arquivo de configuração do s1](mininet_s1_ifconfig.txt)

### 3. Desenho ilustrativo da topologia com todas as informações obtidas no item anterior

![alt text](Imagens/33.png)

### 4. Pings entre diferentes nós

#### Ping entre todos

```bash
pingall
```

#### Ping entre h1 e h125

```bash
h1 ping -c 3 h125
```
![alt text](Imagens/24.png)

#### Ping entre h20 e h50

```bash
h20 ping -c 3 h50
```
![alt text](Imagens/25.png)

#### Ping entre h120 e h122

```bash
h120 ping -c 3 h122
```
![alt text](Imagens/26.png)

### Teste de ping com o comando tcpdump

```bash
tcpdump -i h1-eth0
```
![alt text](Imagens/27.png)

```bash
ping -c 3 10.0.0.1 
```
![alt text](Imagens/28.png)

### Teste com largura de banda de 30Mbs

![alt text](Imagens/29.png)
![alt text](Imagens/30.png)

### Teste com largura de banda de 40Mbs

![alt text](Imagens/31.png)
![alt text](Imagens/32.png)