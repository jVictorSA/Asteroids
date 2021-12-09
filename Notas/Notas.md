# Notas

## 1 - Jogador
Deve ter movimento baseado em inércia;<br/>
Movimento deve ser rotacional em relação orientação e linear em relação à posição Z;<br/>
Deve ter vidas(com máximo de vidas);<br/>
Deve atirar projéteis;<br/>

## 2 - Asteróides
Devem se movimentar linearmente em uma velocidade constante;<br/>
Se acertados devem despedaçar-se em pedaços menores:<br/>
Estes pedaços menores podem virar pedaços ainda menores mas quando um asteróide chegar à um dado tamanho e for acertado será destruído;<br/>
Se tocar o jogador deve matá-lo;<br/>
A instância de um asteróide de ser removida do jogo após sair totalmente da tela do jogo;

## 3 - Pontuação
Deve aumentar assim que um asteróide é acertado;
Um asteróide de tamanho grande deve ter pontuação baixa;
Um asteróide de tamanho médio deve ter pontuação média;
Um asteróide de tamanho pequeno deve ter pontuação alta;

## 4 - Projetéis
Projétil básico é um tiro único;
Projétil gravitacional atrai asteróides dentro de um raio quando detonado;
Projétil explosivo é detonado quando acerta um asteróide e o destrói completamente. Danifica asteróides dentro do raio de explosão;

## - Tela de jogo
Quando o jogador sair por uma extremidade da tela ele deve aparecer na extremidade oposta com mesma orientação e velocidade;
Da mesma forma os projéteis;
