from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import F

from django.utils import timezone

from .models import Choice, Question

from django.db.models import Max
from django.db.models import Count



class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
      """
      Return the last five published questions (not including those set to be
      published in the future).
      """
      latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


      for question in latest_question_list:
      # Obtém todas as escolhas associadas à pergunta atual
        choices = question.choice_set.all()

      # Inicializa variáveis para armazenar a escolha mais votada e o número de votos
        most_voted_choice = None
        max_votes = 0

        # Percorre todas as escolhas
        for choice in choices:
            # Verifica se a escolha atual tem mais votos do que a escolha mais votada atual
            if choice.votes > max_votes:
                # Se sim, atualiza a escolha mais votada e o número de votos
                most_voted_choice = choice
                max_votes = choice.votes

        # Adiciona a escolha mais votada à instância da questão
        question.most_voted_choice = most_voted_choice

      return latest_question_list


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Selecione uma alternativa",
            },
        )
    else:
        # Incrementa os votos para a escolha selecionada
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


