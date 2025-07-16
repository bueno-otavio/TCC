# TCC
CONTROLE SEMAFÓRICO ADAPTATIVO COM MODELOS PREDITIVOS LSTM NO SIMULADOR SUMO
## Instação das dependências
- Faça a instalação do Sumo Simulator
- Faça a instalação do Maven
- Faça a instalação do VSCode
- Faça a instalação do Amazon Corretto ou outro JDK de sua escolha
- Faça a instalação do git

## Guia de instalação
- Faça o clone desse projeto no local desejado
 - git clone https://github.com/gstvpassos/Automacao-Avancada.git

- Em seguida, no diretório do projeto instale as bibliotecas com os comandos Maven (não esqueça de substituir para o diretório em que seu projeto se encontra). Esse comando irá instalar todas as dependências que estão no pom.xml, cujo arquivo se encontra no diretório do comando.
 - mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\junit.jar" -DgroupId="junit" -DartifactId="junit" -Dversion="junit" -Dpackaging="jar" -DgeneratePom=true

mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\libsumo-1.18.0.jar" -DgroupId="libsumo-1.18.0" -DartifactId="libsumo-1.18.0" -Dversion="libsumo-1.18.0" -Dpackaging="jar" -DgeneratePom=true

mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\libsumo-1.18.0-sources.jar" -DgroupId="libsumo-1.18.0-sources" -DartifactId="libsumo-1.18.0-sources" -Dversion="libsumo-1.18.0-sources" -Dpackaging="jar" -DgeneratePom=true

mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\libtraci-1.18.0.jar" -DgroupId="libtraci-1.18.0" -DartifactId="libtraci-1.18.0" -Dversion="libtraci-1.18.0" -Dpackaging="jar" -DgeneratePom=true

mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\libtraci-1.18.0-sources.jar" -DgroupId="libtraci-1.18.0-sources" -DartifactId="libtraci-1.18.0-sources" -Dversion="libtraci-1.18.0-sources" -Dpackaging="jar" -DgeneratePom=true

mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\lisum-core.jar" -DgroupId="lisum-core" -DartifactId="lisum-core" -Dversion="lisum-core" -Dpackaging="jar" -DgeneratePom=true

mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\lisum-gui.jar" -DgroupId="lisum-gui" -DartifactId="lisum-gui" -Dversion="lisum-gui" -Dpackaging="jar" -DgeneratePom=true

mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\TraaS.jar" -DgroupId="TraaS" -DartifactId="TraaS" -Dversion="TraaS" -Dpackaging="jar" -DgeneratePom=true

Após isso realize a instalação limpa das dependências do projeto para que não ocorra nenhum erro
mvn install clean

Por fim com o projeto aberto no VSCode, rode o arquivo App.Java que está em src\main\java\io\sim\
