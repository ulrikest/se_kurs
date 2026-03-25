import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import logging
import click

class VicsekModel:
    def __init__(self, n, d, v, dt, eta):
        self.n = n  # Number of points
        self.d = d  # Distance between points
        self.v = v  # Velocity of points
        self.dt = dt  # Time step
        self.eta = eta  # Noise
        
        # Initialize the positions and angles
        self.r = np.random.random((self.n, 2))
        self.theta = np.random.random(self.n)
        self.counter = 0

    def distance(self, p1, p2):
        return np.sqrt(((p1 - p2) ** 2).sum())

    def update_model(self):
        for i in range(self.n):
            sum_sin = 0
            sum_cos = 0
            neighbours = 0

            for j in range(self.n):
                if i != j:
                    if self.distance(self.r[i], self.r[j]) < self.d:
                        theta_j = 2 * np.pi * self.theta[j]
                        sum_sin += np.sin(theta_j)
                        sum_cos += np.cos(theta_j)
                        neighbours += 1

            if neighbours > 0:
                avg_theta = np.arctan2(sum_sin / neighbours, sum_cos / neighbours)
                self.theta[i] = (avg_theta / (2 * np.pi)) + self.eta * (np.random.rand() - 0.5)

            dx = self.v * self.dt * np.cos(2 * np.pi * self.theta[i])
            dy = self.v * self.dt * np.sin(2 * np.pi * self.theta[i])

            self.r[i, 0] = self.r[i, 0] + dx
            self.r[i, 1] = self.r[i, 1] + dy

            # Boundary conditions
            if self.r[i, 0] > 1:
                self.r[i, 0] = 0
            if self.r[i, 1] > 1:
                self.r[i, 1] = 0
            if self.r[i, 0] < 0:
                self.r[i, 0] = 1
            if self.r[i, 1] < 0:
                self.r[i, 1] = 1

            self.counter += 1

    def animate(self, frame, q):
        self.update_model()

        x = self.r[:, 0]
        y = self.r[:, 1]
        u = np.cos(2 * np.pi * self.theta)
        vv = np.sin(2 * np.pi * self.theta)

        q.set_offsets(np.c_[x, y])
        q.set_UVC(u, vv)

        print("frame", frame, "counter", self.counter)
        return q,

    def run(self):
        fig, ax = plt.subplots(figsize=(6, 6))
        x = self.r[:, 0]
        y = self.r[:, 1]
        u = np.cos(2 * np.pi * self.theta)
        vv = np.sin(2 * np.pi * self.theta)

        q = ax.quiver(x, y, u, vv, angles='xy')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_title("Vicsek Model")

        ani = FuncAnimation(fig, self.animate, frames=200, fargs=(q,), interval=50, blit=True)
        plt.show()


@click.command()
@click.option("--n", default=200, help="Set number of points")
@click.option("--d", default=0.01, help="Set distance between points")
@click.option("--v", default=0.01, help="Set velocity of points")
@click.option("--dt", default=1, help="Set time step")
@click.option("--eta", default=0.1, help="Set noise")    

def main(n, d, v, dt, eta):
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO
    )
    logging.info("Saved to File")
    logging.info("Program Started")
    
    logging.info(f"n = {n}")
    logging.info(f"d = {d}")
    logging.info(f"v = {v}")
    logging.info(f"dt = {dt}")
    logging.info(f"eta = {eta}")
    
    # Create the VicsekModel instance
    vicsek_model = VicsekModel(n, d, v, dt, eta)
    
    # Run the simulation
    vicsek_model.run()

if __name__ == "__main__":
    main()