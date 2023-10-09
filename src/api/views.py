from django.http import JsonResponse
from rest_framework.views import APIView
from gameOfLife.helpers import GameOfLife


class GameView(APIView):

    def post(self, request):
        session_exists = request.session.session_key
        if not session_exists:
            request.session.create()
            game = GameOfLife()
            request.session["game"] = game.get_grid()
        else:
            game = GameOfLife(grid=request.session["game"])
            game.update_grid()
            request.session["game"] = game.get_grid()

        return JsonResponse(game.get_grid(), safe=False)
