% Define facts for articles
article('Estimates of the reproduction ratio from epidemic surveillance may be biased in spatially structured populations',
        'Accurate estimates of the reproduction ratio are crucial for projecting the evolution of an infectious disease epidemic and for guiding the public health response. Here we prove that estimates of the reproduction ratio based on inference from surveillance data can be inaccurate if the population comprises spatially distinct communities, as the space–mobility interplay may hide the true evolution of the epidemic from surveillance data. Consequently, surveillance may underestimate the reproduction ratio over long periods, even mistaking growing epidemics as subsiding. To address this, we use the spectral properties of the matrix describing the spatial epidemic spread to reweight surveillance data. We propose a correction that removes the bias across all epidemic phases. We validate this correction against simulated epidemics and use COVID-19 as a case study. However, our results apply to any epidemic in which mobility is a driver of circulation. Our findings may help improve epidemic monitoring and surveillance and inform strategies for public health responses. Spatial dynamics can obscure epidemic trends from surveillance data, biasing reproduction ratio estimates over long periods. A spectral correction reweights incidence data to remove this bias, thus improving monitoring to inform response strategies.',
        'John Doe', 2020, 'Epidemiology Journal', 45, 3, '123-130',
        ['epidemic', 'reproduction ratio'], '10.1000/epidemiology2020', 
        'http://www.example.com', 500, 'Accurate estimates of the reproduction ratio...', 'English', 'Physics', 'Epidemiology').

article('A study on the spread of infection across different regions',
        'This study presents results from an analysis on the spread of diseases across regions with different population densities and mobility patterns...',
        'Jane Doe', 2021, 'Journal of Public Health', 50, 4, '150-160',
        ['spread', 'infection', 'region'], '10.1001/jph2021', 'http://www.example2.com',
        700, 'This study presents results...', 'English', 'Physics', 'Public Health').

article('Investigating the effects of social distancing on epidemic spread',
        'The research investigates the impact of social distancing measures on the transmission of infectious diseases, particularly COVID-19...',
        'Alice Smith', 2022, 'Health and Society', 55, 2, '101-115',
        ['social distancing', 'epidemic', 'transmission'], '10.1002/health2022', 
        'http://www.example3.com', 300, 'The research investigates...', 'English', 'Physics', 'Public Health').

% Predicate for retrieving articles by topic
articles_in_topic(Topic, Title, Abstract) :-
    article(Title, Abstract, _, _, _, _, _, _, _, _, _, _, _, Topic, _).

% Predicate for retrieving articles with citations greater than a certain threshold
articles_with_citations(Title, Abstract, Citations) :-
    article(Title, Abstract, _, _, _, _, _, _, _, _, _, _, Citations, _, _),
    Citations > 500.

% Predicate for retrieving articles with high attention (more than 500 citations)
high_attention_article(Title, Abstract) :-
    article(Title, Abstract, _, _, _, _, _, _, _, _, _, _, Citations, _, _),
    Citations > 500.

% Predicate for retrieving articles published in the last 30 days
articles_in_last_30_days(Title, Abstract) :-
    article(Title, Abstract, _, _, Year, _, _, _, _, _, _, _, _, _, _),
    current_year(CurrentYear),
    CurrentYear - Year =< 1.

% Helper to get the current year (can be dynamically updated in a real system)
current_year(2024).  % Replace with dynamic current year function if needed.
