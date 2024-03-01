import tkinter

import src.code.simulator as sim


class FactoryGUI:
    def __init__(self):
        self.__root = tkinter.Tk()
        self.__root.title("Factory Simulator")
        self.__root.geometry("500x500")

        # Create the inputs for the simulation
        self.__create_inputs()

        # Create the button to start the simulation
        self.__create_start_button()

        # Create the results label
        self.__create_results_label()

    def __create_inputs(self):
        self.__inputs_frame = tkinter.Frame(self.__root)
        self.__inputs_frame.pack()

        validate_command = self.__root.register(self.__input_validation)

        # Create the N input
        self.__n_label = tkinter.Label(self.__inputs_frame, text="N")
        self.__n_label.grid(row=0, column=0)
        self.__n_entry = tkinter.Entry(
            self.__inputs_frame,
            validate="key",
            validatecommand=(validate_command, "%P"),
        )
        self.__n_entry.insert(0, str(sim.N))
        self.__n_entry.grid(row=0, column=1)

        # Create the S input
        self.__s_label = tkinter.Label(self.__inputs_frame, text="S")
        self.__s_label.grid(row=1, column=0)
        self.__s_entry = tkinter.Entry(
            self.__inputs_frame,
            validate="key",
            validatecommand=(validate_command, "%P"),
        )
        self.__s_entry.insert(0, str(sim.S))
        self.__s_entry.grid(row=1, column=1)

        # Create the Lambda input
        self.__lambd_label = tkinter.Label(self.__inputs_frame, text="Lambda")
        self.__lambd_label.grid(row=2, column=0)
        self.__lambd_entry = tkinter.Entry(
            self.__inputs_frame,
            validate="key",
            validatecommand=(validate_command, "%P"),
        )
        self.__lambd_entry.insert(0, str(sim.LAMBD))
        self.__lambd_entry.grid(row=2, column=1)

        # Create the Mu input
        self.__mu_label = tkinter.Label(self.__inputs_frame, text="Mu")
        self.__mu_label.grid(row=3, column=0)
        self.__mu_entry = tkinter.Entry(
            self.__inputs_frame,
            validate="key",
            validatecommand=(validate_command, "%P"),
        )
        self.__mu_entry.insert(0, str(sim.MU))
        self.__mu_entry.grid(row=3, column=1)

        # Create the Sigma input
        self.__sigma_label = tkinter.Label(self.__inputs_frame, text="Sigma")
        self.__sigma_label.grid(row=4, column=0)
        self.__sigma_entry = tkinter.Entry(
            self.__inputs_frame,
            validate="key",
            validatecommand=(validate_command, "%P"),
        )
        self.__sigma_entry.insert(0, str(sim.SIGMA))
        self.__sigma_entry.grid(row=4, column=1)

        # Create the iterations input
        self.__iterations_label = tkinter.Label(self.__inputs_frame, text="Iterations")
        self.__iterations_label.grid(row=5, column=0)
        self.__iterations_entry = tkinter.Entry(
            self.__inputs_frame,
            validate="key",
            validatecommand=(validate_command, "%P"),
        )
        self.__iterations_entry.insert(0, str(sim.ITERATIONS))
        self.__iterations_entry.grid(row=5, column=1)

        # Create the random values checkbox
        self.__random_values = tkinter.IntVar(value=1 if sim.RANDOM_VALUES else 0)
        self.__random_values_checkbox = tkinter.Checkbutton(
            self.__inputs_frame, text="Random Values", variable=self.__random_values
        )

        self.__random_values_checkbox.grid(row=6, column=0)

    def __create_start_button(self):
        self.__start_button = tkinter.Button(
            self.__root, text="Start Simulation", command=self.__start_simulation
        )
        self.__start_button.pack()

    def __create_results_label(self):
        # Its need to be scrollable
        self.__scrollbar = tkinter.Scrollbar(self.__root, orient="vertical")
        self.__results_text = tkinter.Text(
            self.__root, yscrollcommand=self.__scrollbar.set
        )
        self.__scrollbar.config(command=self.__results_text.yview)
        self.__results_text.config(state="disabled")
        self.__results_text.pack()
        self.__scrollbar.pack(side="right", fill="y")

    def __start_simulation(self):
        self.__update_results_label("Starting simulation", False)
        n = int(self.__n_entry.get())
        s = int(self.__s_entry.get())
        lambd = float(self.__lambd_entry.get())
        mu = float(self.__mu_entry.get())
        sigma = float(self.__sigma_entry.get())
        iterations = int(self.__iterations_entry.get())
        random_values = bool(self.__random_values.get())

        self.__update_results_label(
            f"Running simulation with N={n}, S={s}, Lambda={lambd}, Mu={mu}, Sigma={sigma}, Iterations={iterations}, Random Values={random_values}"
        )

        # Run the simulation
        self.__simulator = sim.Simulator(
            iterations, n, s, lambd, mu, sigma, random_values
        )

        self.__simulator.run()

        self.__results = self.__simulator.get_results()

        self.__update_results_label(
            f"Results:\n{self.__simulator.get_results_as_text()}"
        )

    def __input_validation(self, P: str):
        return (
            P.replace(".", "").isdigit() if P.count(".") == 1 else P.isdigit()
        ) or P == ""

    def __update_results_label(self, text, save_old_text: bool = True):
        old_text = ""
        if save_old_text:
            old_text = self.__results_text.get("1.0", "end")
        self.__results_text.config(state="normal")
        self.__results_text.insert("end", old_text + "\n" + text)
        self.__results_text.config(state="disabled")

    def run(self):
        self.__root.mainloop()
