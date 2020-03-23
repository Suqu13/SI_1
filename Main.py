import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as mpatches
from matplotlib.figure import Figure

from algorithms.EaAlgorithm import EaAlgorithm
from resolvers.CrossoverResolver import CrosserOX
from utils.FileWriter import FileWriter
from utils.Loader import Loader
from resolvers.MutationResolver import InversionMutator, SwapMutator
from utils.PlotDrawer import PlotDrawer
from utils.ProbabilitiesCounter import SimpleProbabilitiesCounter
from resolvers.SelectionResolver import RouletteSelector


def run():
    loader = Loader()
    file_writer = FileWriter()

    if validate():
        try:
            file_name = filename_read.get()
            file_path = 'TSP/' + file_name
            nodes = loader.load(file_path)
            selector = RouletteSelector()
            crosser = CrosserOX()
            if mutator_val.get() == 1:
                mutator = SwapMutator()
            else:
                mutator = InversionMutator()

            ea_algorithm = EaAlgorithm(
                selector=selector,
                mutator=mutator,
                crosser=crosser,
                nodes=nodes,
                population_size=population_size.get(),
                iteration_number=iteration_number.get(),
                population_fraction_from_greedy_indicator=population_fraction_from_greedy_indicator.get() / 100,
                best_population_fraction_to_next_generation_indicator=
                best_population_fraction_to_next_generation_indicator.get() / 100,
                probabilities_counter=SimpleProbabilitiesCounter(),
                crossover_indicator=crossover_indicator.get() / 100,
                mutation_indicator=mutation_indicator.get() / 100)
            try:
                plot_drawer = PlotDrawer()
                statistics = ea_algorithm.run()
                file_writer.write(statistics, file_name)
                plot_drawer.draw(statistics, plotter, received_canvas)
                message.config(text="Success!", fg="#5CB85C")
            except:
                message.config(text="Error during algorithm execution!", fg="#D9534F")
        except:
            message.config(text="Error during file reading!", fg="#D9534F")


def validate_percentage_indicators(indicator_value: float, indicator_entry: tk.Entry) -> bool:
    if indicator_value < 0 or indicator_value > 100:
        indicator_entry.config(highlightbackground="red")
        return False
    indicator_entry.config(highlightbackground="lightgrey")
    return True


def validate_greater_than_zero(value: float, entry: tk.Entry) -> bool:
    if value <= 0:
        entry.config(highlightbackground="red")
        return False
    entry.config(highlightbackground="lightgrey")
    return True


def validate():
    validation_checks = [
        validate_greater_than_zero(population_size.get(), population_size_entry),
        validate_greater_than_zero(iteration_number.get(), iteration_number_entry)]
    return not validation_checks.__contains__(False)


def embed_plot(master):
    figure = Figure(figsize=(5, 5), dpi=100)
    a = figure.add_subplot(111)
    a.set_ylabel('Distance')
    a.set_xlabel('Generation number')
    a.grid()
    best_legend = mpatches.Patch(color="blue", label="Best")
    avg_legend = mpatches.Patch(color="orange", label="Worst")
    worst_legend = mpatches.Patch(color="green", label="Avg")
    a.legend(handles=[best_legend, avg_legend, worst_legend])
    canvas = FigureCanvasTkAgg(figure, master=master)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=3)
    return a, canvas


def create_slider(indicator, label_text):
    pane = tk.Frame(select_source_file_pane)
    pane.pack(side=tk.TOP, fill=tk.BOTH)
    pane.configure(background='#595959')

    label = tk.Label(pane, text=label_text)
    label.pack(side=tk.TOP, fill=tk.BOTH)
    label.configure(background='#595959')

    slider = tk.Scale(select_source_file_pane, variable=indicator, orient=tk.HORIZONTAL, from_=0.0, to=100.0,
                      showvalue=True,
                      resolution=0.25, digits=5)
    slider.pack(side=tk.TOP, fill=tk.BOTH, padx=50, pady=(0, 20))
    slider.configure(background='#595959', troughcolor='white', highlightbackground='#595959')


def create_input(input, label_text) -> tk.Entry:
    pane = tk.Frame(select_source_file_pane)
    pane.pack(side=tk.TOP, fill=tk.BOTH)
    pane.configure(background='#595959')

    label = tk.Label(pane, text=label_text)
    label.pack(side=tk.TOP, fill=tk.BOTH)
    label.configure(background='#595959')

    entry = tk.Entry(pane, textvariable=input, width=25)
    entry.pack(side=tk.TOP, fill=tk.BOTH, padx=50, pady=(0, 10))
    entry.configure(background='white', highlightbackground='#595959', fg='#595959')
    return entry


if __name__ == "__main__":
    FILES = ["berlin11_modified.tsp", "berlin52.tsp", "kroA100.tsp", "kroA150.tsp", "kroA200.tsp"]
    root = tk.Tk()
    root.geometry("1400x900")
    root.title("Evolutionary algorithm")
    root.configure(background='#595959')
    plotter, received_canvas = embed_plot(master=root)

    select_source_file_pane = tk.Frame(root)
    select_source_file_pane.pack(side=tk.RIGHT, fill=tk.BOTH)
    select_source_file_pane.configure(background='#595959')

    select_source_file_label = tk.Label(select_source_file_pane, text="Select source file: ")
    select_source_file_label.pack(side=tk.TOP, fill=tk.BOTH)
    select_source_file_label.configure(background='#595959')

    filename_read = tk.StringVar(root)
    filename_read.set("berlin11_modified.tsp")

    select_source_file_menu = tk.OptionMenu(select_source_file_pane, filename_read, *FILES)
    select_source_file_menu.pack(side=tk.TOP, fill=tk.BOTH, padx=50, pady=(0, 30))
    select_source_file_menu.configure(background='white', fg='#595959')

    mutation_mode_pane = tk.Frame(select_source_file_pane)
    mutation_mode_pane.pack(side=tk.TOP, fill=tk.BOTH)
    mutation_mode_pane.configure(background='#595959')

    mutation_label = tk.Label(mutation_mode_pane, text="Mutation mode: ")
    mutation_label.pack(side=tk.TOP, fill=tk.BOTH)
    mutation_label.configure(background='#595959')

    mutator_val = tk.IntVar(root)
    swap_mutator = tk.Radiobutton(mutation_mode_pane, text="Swap", variable=mutator_val, value=1)
    swap_mutator.select()
    swap_mutator.pack(side=tk.TOP, fill=tk.BOTH)
    swap_mutator.configure(background='#595959', activebackground='#595959', selectcolor='#D4A72B',
                           highlightthickness='0')
    inversion_mutator = tk.Radiobutton(mutation_mode_pane, text="Inversion", variable=mutator_val, value=2)
    inversion_mutator.select()
    inversion_mutator.pack(side=tk.TOP, fill=tk.BOTH, pady=(0, 20))
    inversion_mutator.configure(background='#595959', activebackground='#595959', selectcolor='#D4A72B',
                                highlightthickness='0')

    iteration_number = tk.IntVar(root)
    iteration_number_entry = create_input(iteration_number, "Iterations number: ")

    population_size = tk.IntVar(root)
    population_size_entry = create_input(population_size, "Population size: ")

    crossover_indicator = tk.DoubleVar(root)
    create_slider(crossover_indicator, "Crossing propability [%]:")

    mutation_indicator = tk.DoubleVar(root)
    create_slider(mutation_indicator, "Mutation probability [%]: ")

    population_fraction_from_greedy_indicator = tk.DoubleVar(root)
    create_slider(population_fraction_from_greedy_indicator, "Inital greedy solution indicator propability [%]: ")

    best_population_fraction_to_next_generation_indicator = tk.DoubleVar(root)
    create_slider(best_population_fraction_to_next_generation_indicator, "Elitarism indicator [%]: ")

    message_pane = tk.Frame(select_source_file_pane)
    message_pane.pack(side=tk.TOP, fill=tk.BOTH)

    message = tk.Label(message_pane, justify="center", width=40, font=30)
    message.pack(side=tk.TOP, fill=tk.BOTH)
    message.configure(background='#595959')

    button_pane = tk.Frame(select_source_file_pane)
    button_pane.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=50, pady=(0, 30))
    button_pane.configure(background='#595959')

    tk.Button(button_pane, text="Run!", width=25, command=run, bg="#D4A72B",
              activebackground="#E1C26C",
              activeforeground="#ffffff",
              fg="#ffffff").pack(side=tk.TOP, fill=tk.BOTH)

    root.mainloop()
