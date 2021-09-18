from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
import csv
from .forms import UploadFileForm
from .models import Upload

from django.template import RequestContext
from django.http import HttpResponseRedirect
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer



def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Upload(title=request.POST['title'], file=request.FILES['file'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()

    # Load documents for the list page
    documents = Upload.objects.all()

    # Render list page with the documents and the form
    return render(request, 'index.html', {'documents': documents, 'form': form})


def render_csv(request):
    lines = []
    last_table = Upload.objects.last()
    with open(f'media/{last_table.file}', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for line in reader:
            lines.append(
                line
            )

    documentA = lines[0][0]

    bagOfWordsA = documentA.split(' ')

    uniqueWords = set(bagOfWordsA)

    numOfWordsA = dict.fromkeys(uniqueWords, 0)

    for word in bagOfWordsA:
        numOfWordsA[word] += 1

    def computeTF(wordDict, bagOfWords):
        tfDict = {}
        bagOfWordsCount = len(bagOfWords)
        for word, count in wordDict.items():
            tfDict[word] = count / float(bagOfWordsCount)
        return tfDict

    TF = computeTF(numOfWordsA, bagOfWordsA)

    value_of_TF = []
    for t in TF:
        value_of_TF.append(TF[t])

    def computeIDF(documents):
        import math
        N = len(documents)

        idfDict = dict.fromkeys(documents[0].keys(), 0)
        for document in documents:
            for word, val in document.items():
                if val > 0:
                    idfDict[word] += 1

        for word, val in idfDict.items():
            idfDict[word] = math.log(N / float(val))
        return idfDict

    idf = computeIDF([numOfWordsA])

    list_idf = []

    for item in idf:
        list_idf.append(idf[item])

    return render(request, 'read.html', {'text': TF, 'value_of_TF': value_of_TF, 'idf': list_idf})
