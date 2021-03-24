from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from escola.models import Aluno, Curso, Matricula
from escola.serializer import (
        AlunoSerializer, CursoSerializer, 
        MatriculaSerializer, ListaMatriculasAlunoSerializer,
        ListaAlunosMatriculadosSerializer
    )


class AlunosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os alunos
    """

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

    # configuracoes de autenticacao e permissao
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """
    Exibindo todos os cursos
    """

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # configuracoes de autenticacao e permissao
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Listando todas as matrículas
    """

    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

    # configuracoes de autenticacao e permissao
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """
    Listando as matrículas de um aluno ou aluna
    """

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

    # configuracoes de autenticacao e permissao
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaAlunosMatriculados(generics.ListAPIView):
    """
    Listando alunos e alunas matriculados em um curso
    """
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer

    # configuracoes de autenticacao e permissao
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
