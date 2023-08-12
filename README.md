# generate_customized_cover_letter
Natürlich, hier ist ein Beispiel für die Verwendung des Programms in einem Use Case:

**Use Case: Personalisiertes Anschreiben für eine Bewerbung**

Annahme: Sie sind auf der Suche nach einer neuen Stelle als Softwareentwickler bei einem Technologieunternehmen. Sie haben eine Stellenanzeige gefunden, die Ihren Fähigkeiten und Interessen entspricht. Sie möchten ein personalisiertes Anschreiben erstellen, um Ihre Eignung für die Position zu unterstreichen.

1. **Stellenanzeige**: Kopieren Sie den Text der Stellenanzeige, die Sie gefunden haben, und fügen Sie ihn in die Variable `stellenanzeige_text` im Skript ein.

2. **Ihr Profil**: Erfassen Sie Informationen über sich selbst, einschließlich Ihrer beruflichen Erfahrung, Fähigkeiten und Qualifikationen. Fügen Sie diese Informationen in die Variable `bewerber_profil` im Skript ein.

3. **PDF-Datei**: Speichern Sie Ihren Lebenslauf als PDF-Datei und speichern Sie den Pfad zur Datei in der Variable `pdf_path` im Skript.

4. **Anpassung des Anschreibens**: Führen Sie das Skript aus, indem Sie den Befehl `/usr/bin/python3.10 /home/oem/Dokumente/BewerbungsSchreiberAuto.py` in Ihrer Terminalanwendung ausführen. Das Skript extrahiert den Text aus der PDF-Datei und berechnet die Ähnlichkeit zwischen dem Stellenangebot, Ihrem Profil und dem extrahierten Text.

5. **Anschreiben generieren**: Das Skript generiert ein personalisiertes Anschreiben basierend auf den Ähnlichkeiten. Die Jinja2-Vorlage wird verwendet, um die relevanten Informationen aus der Stellenanzeige, Ihrem Profil und dem extrahierten Text in das Anschreiben einzufügen.

6. **Anschreiben überprüfen**: Überprüfen Sie die generierte Ausgabe des Anschreibens. Passen Sie die Platzhalter (z. B. Jobtitel, Firmenname, Ihr Name) an und fügen Sie den Rest des Anschreibens in die Jinja2-Vorlage ein, um ein vollständiges Anschreiben zu erstellen.

7. **Bewerbung einreichen**: Verwenden Sie das generierte Anschreiben zusammen mit Ihrem Lebenslauf, um sich auf die ausgeschriebene Stelle zu bewerben.

Durch die Verwendung dieses Programms können Sie ein personalisiertes Anschreiben erstellen, das speziell auf die Anforderungen der Stellenanzeige zugeschnitten ist und Ihre Eignung für die Position hervorhebt. Dies kann Ihnen helfen, einen positiven Eindruck bei potenziellen Arbeitgebern zu hinterlassen und Ihre Chancen auf eine Einladung zum Vorstellungsgespräch zu erhöhen.
