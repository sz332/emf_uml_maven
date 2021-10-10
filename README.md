# EMF/UML2 with maven support 
Install eclipse emf and uml jars into local maven repository

When people want to start playing with the EMF/UML tools provided by the Eclipse Project, they will very soon realize that the common way of using maven or grandle to import the necessary dependecies in their project does not work. The reason for is that the devs at Eclipse simply don't update the maven repositories with the latest version of files, and hunting for the necessary jars from various repos just does not gets the job done (spent a couple of hours on it). 

Therefore, my solution was to download the EMF and UML packages directly from the eclipse site, and wrote a very simply python code that extract the archives and installs each and every jar file with their corresponding source files into my local maven repository.

