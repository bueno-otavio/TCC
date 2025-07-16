# Instação das dependências

1. Faça a instalação do Sumo Simulator  
2. Faça a instalação do Maven  
3. Faça a instalação do VSCode  
4. Faça a instalação do Amazon Corretto ou outro JDK de sua escolha  
5. Faça a instalação do git  

---

# Guia de instalação

1. **Faça o clone desse projeto no local desejado:**

   ```bash
   git clone https://github.com/gstvpassos/Automacao-Avancada.git
   ```

2. **No diretório do projeto, instale as bibliotecas com os comandos Maven**  
   (substitua `C:\Users\USER\PATH` pelo caminho correto no seu ambiente).  
   Esses comandos instalarão todas as dependências que estão no `pom.xml` — o arquivo deve estar no diretório em que você executa os comandos.

   ```bash
   mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\junit.jar" -DgroupId="junit" -DartifactId="junit" -Dversion="junit" -Dpackaging="jar" -DgeneratePom=true
   ```

   ```bash
   mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\libsumo-1.18.0.jar" -DgroupId="libsumo-1.18.0" -DartifactId="libsumo-1.18.0" -Dversion="libsumo-1.18.0" -Dpackaging="jar" -DgeneratePom=true
   ```

   ```bash
   mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\libsumo-1.18.0-sources.jar" -DgroupId="libsumo-1.18.0-sources" -DartifactId="libsumo-1.18.0-sources" -Dversion="libsumo-1.18.0-sources" -Dpackaging="jar" -DgeneratePom=true
   ```

   ```bash
   mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\libtraci-1.18.0.jar" -DgroupId="libtraci-1.18.0" -DartifactId="libtraci-1.18.0" -Dversion="libtraci-1.18.0" -Dpackaging="jar" -DgeneratePom=true
   ```

   ```bash
   mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\libtraci-1.18.0-sources.jar" -DgroupId="libtraci-1.18.0-sources" -DartifactId="libtraci-1.18.0-sources" -Dversion="libtraci-1.18.0-sources" -Dpackaging="jar" -DgeneratePom=true
   ```

   ```bash
   mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\lisum-core.jar" -DgroupId="lisum-core" -DartifactId="lisum-core" -Dversion="lisum-core" -Dpackaging="jar" -DgeneratePom=true
   ```

   ```bash
   mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\lisum-gui.jar" -DgroupId="lisum-gui" -DartifactId="lisum-gui" -Dversion="lisum-gui" -Dpackaging="jar" -DgeneratePom=true
   ```

   ```bash
   mvn install:install-file -Dfile="C:\Users\USER\PATH\lib\sumo\TraaS.jar" -DgroupId="TraaS" -DartifactId="TraaS" -Dversion="TraaS" -Dpackaging="jar" -DgeneratePom=true
   ```

3. **Após isso, realize a instalação limpa das dependências do projeto para evitar erros:**

   ```bash
   mvn install clean
   ```

4. **Por fim, com o projeto aberto no VSCode, rode o arquivo `app.py` e em seguida `App.java` que está em `src\main\java\io\sim\`.**
