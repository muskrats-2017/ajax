from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

class Index(View):
	template = 'deaf/index.html'

	def get(self, request):
		return render(request, self.template)

	def post(self, request):
		if request.POST.get('say', '').isupper():
			say = "hi tom!"
		else:
			say = "I cant hear you"

		# return JsonResponse({'say': say, 'said': request.POST.get('say', '')})
		return render(request, 'deaf/said.html', {
			'said': request.POST.get('say', ''),
			'say': say
		});
