




        query_prng = np.random.RandomState(seed=99)
        c_seed = int(np.random.RandomState(query_prng.randint(2**32)
                                      ).choice(circuit_seeds))
        noise_seed = int(query_prng.randint(2**32))
        circuit = factory.make(c_seed, noise_seed)
        state_vector = cirq.final_wavefunction(circuit)
