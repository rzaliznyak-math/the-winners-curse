observed_power = np.mean(
    np.where(
        alt_simulations > significance_threshold,
        1,
        0,
    )
)
prob_above_effect = np.mean(
    np.where(
        alt_simulations
        > delta_to_control_planned,
        1,
        0,
    )
)

pr_over_estimate_statssig = (
    prob_above_effect / observed_power
)

pr_over_estimate_statssig
