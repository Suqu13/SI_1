from tkinter import Entry, OptionMenu, Label, Tk, StringVar, IntVar, Radiobutton, Button

from Algorithms.EaAlgorithm import EaAlgorithm
from CrossoverResolver import CrosserOX
from Loader import Loader
from MutationResolver import InversionMutator, SwapMutator
from ProbabilitiesCounter import SimpleProbabilitiesCounter
from SelectionResolver import RouletteSelector


def run():
    loader = Loader()

    if validate():
        try:
            file_path = 'TSP/' + filename_read.get()
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
                population_fraction_from_greedy=population_fraction_from_greedy.get() / 100,
                best_population_fraction_to_next_generation=best_population_fraction_to_next_generation.get() / 100,
                probabilities_counter=SimpleProbabilitiesCounter(),
                crossover_indicator=crossover_indicator.get() / 100,
                mutation_indicator=mutation_indicator.get() / 100)

            try:
                ea_algorithm.run()
                message.config(text="Success!", fg="#5CB85C")
            except:
                message.config(text="Error during algorithm execution!", fg="#D9534F")
        except:
            message.config(text="Error during file reading!", fg="#D9534F")


def validate_percentage_indicators(indicator_value: float, indicator_entry: Entry) -> bool:
    if indicator_value < 0 or indicator_value > 100:
        indicator_entry.config(highlightbackground="red")
        return False
    indicator_entry.config(highlightbackground="lightgrey")
    return True


def validate_greater_than_zero(value: float, entry: Entry) -> bool:
    if value <= 0:
        entry.config(highlightbackground="red")
        return False
    entry.config(highlightbackground="lightgrey")
    return True


def validate():
    validation_checks = [
        validate_greater_than_zero(population_size.get(), population_size_entry),
        validate_greater_than_zero(iteration_number.get(), iteration_number_entry),
        validate_percentage_indicators(crossover_indicator.get(), crossover_indicator_entry),
        validate_percentage_indicators(mutation_indicator.get(), mutation_indicator_entry),
        validate_percentage_indicators(best_population_fraction_to_next_generation.get(),
                                       best_population_fraction_to_next_generation_entry),
        validate_percentage_indicators(population_fraction_from_greedy.get(), population_fraction_from_greedy_entry)]
    return not validation_checks.__contains__(False)


if __name__ == "__main__":
    FILES = ["berlin11_modified.tsp", "berlin52.tsp", "kroA100.tsp", "kroA150.tsp", "kroA200.tsp"]
    root = Tk()
    root.geometry("700x480")
    root.title("Evolutionary algorithm")

    Label(root, text="Filename of file to read: ").place(x=15, y=10)
    filename_read = StringVar(root)
    filename_read.set("berlin11_modified.tsp")
    opt = OptionMenu(root, filename_read, *FILES)
    opt.place(x=500, y=10)

    Label(root, text="Mutation mode: ").place(x=15, y=100)
    mutator_val = IntVar(root)
    def_mutator = Radiobutton(root, text="Swap", variable=mutator_val, value=1)
    def_mutator.select()
    def_mutator.place(x=500, y=100)
    Radiobutton(root, text="Inversion", variable=mutator_val, value=2).place(x=580, y=100)

    Label(root, text="Population size: ").place(x=15, y=130)
    population_size = IntVar(root)
    population_size_entry = Entry(root, textvariable=population_size, width=25)
    population_size_entry.place(x=500, y=130)

    Label(root, text="Iterations number: ").place(x=15, y=160)
    iteration_number = IntVar(root)
    iteration_number_entry = Entry(root, textvariable=iteration_number, width=25)
    iteration_number_entry.place(x=500, y=160)

    Label(root, text="Crossover probability [0-100]%: ").place(x=15, y=190)
    crossover_indicator = IntVar(root)
    crossover_indicator_entry = Entry(root, textvariable=crossover_indicator, width=25)
    crossover_indicator_entry.place(x=500, y=190)

    Label(root, text="Mutation probability [0-100]%: ").place(x=15, y=220)
    mutation_indicator = IntVar(root)
    mutation_indicator_entry = Entry(root, textvariable=mutation_indicator, width=25)
    mutation_indicator_entry.place(x=500, y=220)

    Label(root, text="% of best individuals copying to next generation (elitism) [0-100]%: ").place(x=15, y=280)
    best_population_fraction_to_next_generation = IntVar(root)
    best_population_fraction_to_next_generation_entry = Entry(root,
                                                              textvariable=best_population_fraction_to_next_generation,
                                                              width=25)
    best_population_fraction_to_next_generation_entry.place(x=500, y=280)

    Label(root, text="% of initial population which contain individuals from greedy algorithm [0-100]%: ") \
        .place(x=15, y=310)
    population_fraction_from_greedy = IntVar(root)
    population_fraction_from_greedy_entry = Entry(root, textvariable=population_fraction_from_greedy, width=25)
    population_fraction_from_greedy_entry.place(x=500, y=310)

    Label(root, text="Filename of file to write data: ").place(x=15, y=340)
    filename_write = StringVar(root)
    filename_write_entry = Entry(root, textvariable=filename_write, width=25)
    filename_write_entry.place(x=500, y=340)

    Button(root, text="Run!", width=25, command=run, bg="#337AB7",
           activebackground="#5BC0DE",
           activeforeground="#ffffff",
           fg="#ffffff").place(x=260, y=370)

    message = Label(root, justify="center", width=80, font=30)
    message.place(x=0, y=430)

    root.mainloop()
