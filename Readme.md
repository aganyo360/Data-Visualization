# Plotting a simple Line graph

## Steps

### prequisities

#### install packages

    pip install matplotlib

## plotting a simple line graph

<code>
    import matplotlib.pyplot as plt

    squares =[1,4,9,16,25]
    fig, ax = plt.subplots()
    ax.plot(squares)

    plt.show
</code>

## Explanation
    1. first import the pyplot module using the alias plt so we don’t have to type pyplot repeatedly

