prior_mean = 0
prior_se = 0.0025
(
    posterior_mean,
    posterior_se,
) = combine_prior_and_likelihood(
    prior_mean, prior_se, delta, se_delta
)

plot_distributions_cdf_only(
    prior_mean=prior_mean,
    prior_se=prior_se,
    like_mean=delta,
    like_se=se_delta,
    post_mean=posterior_mean,
    post_se=posterior_se,
    metric_name="Conversions",
)
