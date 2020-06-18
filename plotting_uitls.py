def vector_plot(tvects,is_vect=True,orig=[0,0,0]):
    """Plot vectors using plotly"""

    if is_vect:
        if not hasattr(orig[0],"__iter__"):
            coords = [[orig,np.sum([orig,v],axis=0)] for v in tvects]
        else:
            coords = [[o,np.sum([o,v],axis=0)] for o,v in zip(orig,tvects)]
    else:
        coords = tvects

    data = []
    for i,c in enumerate(coords):
        X1, Y1, Z1 = zip(c[0])
        X2, Y2, Z2 = zip(c[1])
        vector = go.Scatter3d(x = [X1[0],X2[0]],
                              y = [Y1[0],Y2[0]],
                              z = [Z1[0],Z2[0]],
                              marker = dict(size = [0,5],
                                            color = ['blue'],
                                            line=dict(width=5,
                                                      color='DarkSlateGrey')),
                              name = 'Vector'+str(i+1))
        data.append(vector)

    layout = go.Layout(
             margin = dict(l = 4,
                           r = 4,
                           b = 4,
                           t = 4)
                  )
    fig = go.Figure(data=data,layout=layout)
    fig.show()
    
def proj_onto_line(vect_a, vect_b):
    
    a1, a2, a3 = vect_a
    b1, b2, b3 = vect_b
    
    vect_a = np.array(vect_a)
    
    vect_b = np.array(vect_b)
    
    P_a = (vect_a * vect_a.T)/vect_a.dot(vect_a.T)
    
    print(proj_a.dot(vect_b.T))
    
    p1, p2, p3 = proj_a.dot(vect_b.T)
    
    
    
    
    data = []
    vector = go.Scatter3d(x = [0,a1],
                          y = [0,a2],
                          z = [0,a3],
                          marker = dict(size = [0,5],
                                        color = ['blue'],
                                        line=dict(width=5,
                                        color='DarkSlateGrey')),
                        name = 'a')
                               
    data.append(vector)
    
    vector = go.Scatter3d(x = [0,b1],
                          y = [0,b2],
                          z = [0,b3],
                          marker = dict(size = [0,5],
                                        color = ['blue'],
                                        line=dict(width=5,
                                        color='DarkSlateGrey'
                                                 )),
                        name = 'b')
                               
               
    data.append(vector)
    
    
    vector = go.Scatter3d(x = [0,p1],
                          y = [0,p2],
                          z = [0,p3],
                          marker = dict(size = [0,5],
                                        color = ['blue'],
                                        line=dict(width=5,
                                        color='DarkSlateGrey'
                                                 )),
                        name = 'projection')
    
    data.append(vector)

    
    vector = go.Scatter3d(x = [b1,p1],
                          y = [b2,p2],
                          z = [b3,p3],
                          marker = dict(size = [0,5],
                                        color = ['blue'],
                                        line=dict(width=5,
                                        color='DarkSlateGrey'
                                                 )),
                        name = 'error')
    
    data.append(vector)
    
    layout = go.Layout(
             margin = dict(l = 4,
                           r = 4,
                           b = 4,
                           t = 4)
                  )
    fig = go.Figure(data=data,layout=layout)
    fig.show()
                               
                               
