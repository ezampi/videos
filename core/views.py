from django.shortcuts import render

def index(request):
    return render(request, template_name='core/index.html')

def list_videos(request):
    return render(request, template_name= 'core/videos.html')

def player(request, slug):
    return render(request,'core/player.html', {
                             'video': {
                                "titulo": "As melhores palestras estão aqui.",
                                "subtitulo" : "subtitulo",
                                "descricao_curta" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Labore, eos, voluptatibus tenetur modi velit quae laboriosam autem voluptas iusto vitae nesciunt tempora possimus quaerat. Explicabo, quaerat rerum amet fugiat dolore.",
                                "descricao" : "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Labore, eos, voluptatibus tenetur modi velit quae laboriosam autem voluptas iusto vitae nesciunt tempora possimus quaerat. Explicabo, quaerat rerum amet fugiat dolore." * 20
                             }
                          })
