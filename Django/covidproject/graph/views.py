from django.shortcuts import render
from graph import script
from graph.models import StateInfo

def insert_data(df, c, r, d):
    for index, row in df.iterrows():
        # print (index, row["Confirmed"], row["Recovered"])
        # print(c.get(key = index))
        u = StateInfo.objects.get_or_create(state_name = index, confirmed = row['Confirmed'] ,
        recovered = row['Recovered'], deceased = row['Deceased'],
        tc = c.get(key = index), tr = r.get(key = index), td = d.get(key = index))[0]
        # u.save()

# Create your views here.
def index(request):
    [df, df_MC, df_MR, df_MD] = script.start()
    insert_data(df, df_MC, df_MR, df_MD)
    s = StateInfo.objects.order_by('state_name')
    my_dict = {'state_table' : s}
    return render(request, 'graph/index.html', context = my_dict)
