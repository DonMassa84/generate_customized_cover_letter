import nltk
nltk.download('stopwords')
nltk.download('punkt')
import PyPDF2
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from jinja2 import Template

# Beispiel-Stellenanzeige und Bewerberprofil
stellenanzeige_text = """
Hier kommen Sie ins Spiel
Übernehmen Sie die Mitverantwortung für den Betrieb einer der neusten und modernsten Software-
Umgebung für Lotteriegesellschaften in Deutschland; dazu gehört die Ausführung von Anwendungen,
Prozeduren, Triggern und Services im Rahmen des operativen Betriebs für die Spielesysteme
...
Regelmäßige MitarbeitereventsKontakt:
Ihre vollständigen Bewerbungsunterlagen senden Sie bitte einschließlich Angaben zu Gehaltsvorstellung und
möglichen Eintrittstermin an unsere Personalabteilung.
...
www.lotto-hh.de...
"""  # Fügen Sie den tatsächlichen Text der Stellenanzeige ein

bewerber_profil = """
Daniel Massa ist ein fachlich versierter Fachinformatiker für Anwendungsentwicklung mit umfangreicher internationaler Erfahrung
in leitenden Positionen. Er hat seinen Hauptsitz in Hamburg und ist derzeit in einer Umschulung zum Fachinformatiker für Anwen-
dungsentwicklung. Seine technischen Fähigkeiten umfassen die Arbeit mit Microsoft und Linux, HTML5, Java, PHP, Elixir von Erlang
und SQL-Datenbanken. Er hat seine Fähigkeiten durch Praktika bei Grassau GmbH und aidminutes GmbH in Hamburg weiter verfei-
nert.
...
machen ihn zu
einem wertvollen Mitglied jedes Teams.
"""  # Fügen Sie das tatsächliche Bewerberprofil ein

# PDF-Extraktion (unverändert)

def extract_text_from_pdf(pdf_path):
    extracted_text = ""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                extracted_text += page.extract_text()
    except Exception as e:
        print("Error while extracting text from PDF:", str(e))
        extracted_text = None

    return extracted_text

# NLP-Verarbeitung (unverändert)

def preprocess_text(text):
    sentences = sent_tokenize(text)
    words = [word for sent in sentences for word in word_tokenize(sent)]
    words = [word.lower() for word in words if word.isalnum()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return ' '.join(words)

# TF-IDF Ähnlichkeit (unverändert)

def calculate_similarity(text1, text2):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([text1, text2])
    similarity_matrix = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity_matrix[0][0]

# Hauptfunktion (unverändert)

def generate_customized_cover_letter(pdf_path, job_description, applicant_profile):
    extracted_text = extract_text_from_pdf(pdf_path)
    preprocessed_job_desc = preprocess_text(job_description)
    preprocessed_applicant_profile = preprocess_text(applicant_profile)

    job_desc_similarity = calculate_similarity(extracted_text, preprocessed_job_desc)
    applicant_profile_similarity = calculate_similarity(extracted_text, preprocessed_applicant_profile)

    # Hier können Sie Logik hinzufügen, um die passenden Abschnitte für die Bewerbung zu erstellen
    # basierend auf den Ähnlichkeiten zwischen Stellenanzeige, Bewerberprofil und extrahiertem Text.

    # Beispiel-Jinja2-Vorlage für die Bewerbung
    template_string = """
    Sehr geehrte Damen und Herren,

    ich bin äußerst interessiert an der ausgeschriebenen Position als {{ job_title }} 
    bei {{ company_name }}.
    
    Die Möglichkeit, Teil eines internationalen Teams zu sein und verschiedene Einkaufsprozesse 
    von der {{ company_name }} zu sichern, hat mein besonderes Interesse geweckt.
    
    {{ company_name }} fungiert als zentraler IT-Dienstleister und ist verantwortlich für
    Auswahl, Bereitstellung, Betrieb und Weiterentwicklung von IT-Infrastrukturen, IT-
    Plattformen und Business-Anwendungen. 
    Als {{ job_title }}  übernehme ich die Verantwortung 
    für das Monitoring der Datenverarbeitung und unterstütze den operativen Betrieb bezogen auf
    Einkaufsprozesse. Dabei trage ich zur kontinuierlichen Optimierung der
    Supportprozesse sowie zum proaktiven und reaktiven Problem Management bei,
    um nachhaltig Störungen zu vermeiden.
    
    Mit einer abgeschlossenen IT-Ausbildung bringe ich das erforderliche technische
    Grundwissen und IT-Kenntnisse mit. Zudem verfüge ich über Prozesskenntnisse
    aus den Bereichen Einkauf und Stammdatenmanagement. Meine ausgeprägte
    Analysefähigkeit, Kommunikationsstärke, Kundenorientierung und Freude an
    Teamarbeit machen mich zu einem wertvollen Ansprechpartner im
    internationalen Team.
    
    Die Möglichkeit, in einem dynamischen und schnell wachsenden
    Handelsunternehmen zu arbeiten, bietet mir eine spannende Umgebung, um
    mich fachlich und persönlich weiterzuentwickeln. Die flexible Arbeitszeitgestaltung 
    und die Option des mobilen Arbeitens tragen zur
    Vereinbarkeit von Beruf und Privatleben bei.
    
    
    Ich freue mich darauf, eine Fähigkeiten als {{ job_title }}
    einzubringen und dazu beizutragen, die Einkaufsprozesse bei Schwarz IT
    erfolgreich zu unterstützen.
    Für weitere Informationen stehe ich Ihnen gerne zur Verfügung und freue mich
    auf die Möglichkeit eines persönlichen Gesprächs.

    Mit freundlichen Grüßen,
    {{ applicant_name }}
    """

    template = Template(template_string)
    cover_letter = template.render(job_title="Fachinformatiker Anwendungsentwickler", company_name="LOTTO Hamburg", applicant_name="Daniel Massa")

    return cover_letter

# Verwendung der Hauptfunktion
job_description = stellenanzeige_text
applicant_profile = bewerber_profil
pdf_path = "/home/oem/Dokumente/LOTTO_Hamburg.pdf"  # Fügen Sie den tatsächlichen Pfad zur PDF-Datei ein

customized_cover_letter = generate_customized_cover_letter(pdf_path, job_description, applicant_profile)
print(customized_cover_letter)

