from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer
from django.contrib.auth.decorators import login_required

def preguntas(request):
    questions = Question.objects.all()
    return render(request, 'preguntas.html', {'questions': questions})


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Guardar la pregunta y sus opciones
            question = Question()
            question.question_type = form.cleaned_data['question_type']
            question.text = form.cleaned_data['text']
            question.option_a = form.cleaned_data['option_a']
            question.option_b = form.cleaned_data['option_b']
            question.option_c = form.cleaned_data['option_c']
            question.option_d = form.cleaned_data['option_d']
            question.correct_answer = form.cleaned_data['correct_answer']
            question.save()
        return redirect('preguntas')
    else:
        form = QuestionForm()
    return render(request, 'crear_pregunta.html', {'form': form})


@login_required 
def formulario(request):
    # Obtener todas las preguntas
    questions = Question.objects.all()
    if request.method == 'POST':
        
        for pregunta in questions:
            question_id = request.POST.get(f'question_id_{pregunta.id}')
            text_answer = request.POST.get(f'text_answer_{pregunta.id}')
            option_answer = request.POST.get(f'option_answer_{pregunta.id}')
            # if form.is_valid():
            # Guardar la respuesta
            answer = Answer()
            # answer question es id de la pregunta
            answer.question = Question.objects.get(id=question_id)
            # answer user es el usuario que esta respondiendo la pregunta
            answer.user = request.user
            answer.text_answer = text_answer
            # answer option_answer es la opcion que el usuario selecciono, puede ser null
            # si es nulo y por lo tanto diferente de a, b, c, d, entonces no se guarda
            if option_answer in ['a', 'b', 'c', 'd']:
                answer.option_answer = option_answer

            answer.save()



        return redirect('agradecimientos')
    else:
        form = AnswerForm()

    return render(request, 'formulario.html', {'form': form, 'questions': questions})






def delete_question(request, id):
    question = Question.objects.get(id=id)
    question.delete()
    return redirect('preguntas')

# def agradecimientos, este tendra un mensaje de agradecimiento por haber respondido la encuesta
def agradecimientos(request):
    return render(request, 'agradecimientos.html')





# def update_question, este tendra un formulario para actualizar la pregunta
def update_question(request, id):

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        question = Question.objects.get(id=id)
        tipo = question.question_type
 
        
        if form.is_valid():
            # guardar la pregunta y sus opciones, usando el id de la pregunta
            if tipo == 'text':
                #form = QuestionForm(initial={'text': question.text})
                # guardar las preguntas con el formulario de texto
                question.text = form.cleaned_data['text']
                question.save()
                return redirect('preguntas')

            else:
                #form = QuestionForm(initial={'text': question.text, 'option_a': question.option_a, 'option_b': question.option_b, 'option_c': question.option_c, 'option_d': question.option_d, 'correct_answer': question.correct_answer})
                question.text = form.cleaned_data['text']
                question.option_a = form.cleaned_data['option_a']
                question.option_b = form.cleaned_data['option_b']
                question.option_c = form.cleaned_data['option_c']
                question.option_d = form.cleaned_data['option_d']
                question.correct_answer = form.cleaned_data['correct_answer']
                question.save()
                return redirect('preguntas')
        else:
            if tipo == 'text':
                form = QuestionForm(initial={'text': question.text})
            else:
                form = QuestionForm(initial={'text': question.text, 'option_a': question.option_a, 'option_b': question.option_b, 'option_c': question.option_c, 'option_d': question.option_d, 'correct_answer': question.correct_answer})
        
   
    return render(request, 'update_question.html', {'form': form, 'question': question, 'tipo': tipo})



