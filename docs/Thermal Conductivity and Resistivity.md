# Thermal Conductivity

> Capacity of a material to conduct heat

## Physical Properties

**Thermal conductivity**
- **Symbol**: $\kappa$
- **Unit**: watt per meter-kelvin (W/(m⋅K))
- **Base units**: kg⋅m⋅s$^{-3}$⋅K$^{-1}$
- **Dimension**: M$^1$L$^1$T$^{-3}$Θ$^{-1}$

**Thermal resistivity**
- **Symbol**: $\rho$
- **Unit**: kelvin-meter per watt (K⋅m/W)
- **Base units**: kg$^{-1}$⋅m$^{-1}$⋅s$^{3}$⋅K
- **Dimension**: M$^{-1}$L$^{-1}$T$^{3}$Θ

The **thermal conductivity** of a material is a measure of its ability to [conduct heat](https://en.wikipedia.org/wiki/Heat_conduction). It is commonly denoted by $k$, $\lambda$, or $\kappa$ and is measured in W·m$^{-1}$·K$^{-1}$.

Heat transfer occurs at a lower rate in materials of low thermal conductivity than in materials of high thermal conductivity. For instance, metals typically have high thermal conductivity and are very efficient at conducting heat, while the opposite is true for [insulating materials](https://en.wikipedia.org/wiki/Insulating_materials) such as [mineral wool](https://en.wikipedia.org/wiki/Mineral_wool) or [Styrofoam](https://en.wikipedia.org/wiki/Styrofoam). Metals have this high thermal conductivity due to free electrons facilitating heat transfer. Correspondingly, materials of high thermal conductivity are widely used in [heat sink](https://en.wikipedia.org/wiki/Heat_sink) applications, and materials of low thermal conductivity are used as [thermal insulation](https://en.wikipedia.org/wiki/Thermal_insulation). The reciprocal of thermal conductivity is called **thermal resistivity**.

The defining equation for thermal conductivity is $\mathbf{q} = - k \nabla T$, where $\mathbf{q}$ is the [heat flux](https://en.wikipedia.org/wiki/Heat_flux), $k$ is the thermal conductivity, and $\nabla T$ is the [temperature gradient](https://en.wikipedia.org/wiki/Temperature_gradient). This is known as [Fourier's law](https://en.wikipedia.org/wiki/Heat_conduction#Fourier's_law) for heat conduction. Although commonly expressed as a [scalar](https://en.wikipedia.org/wiki/Scalar_(physics)), the most general form of thermal conductivity is a second-rank [tensor](https://en.wikipedia.org/wiki/Tensor). However, the tensorial description only becomes necessary in materials which are [anisotropic](https://en.wikipedia.org/wiki/Anisotropic).

## Definition

### Simple definition

![Thermal conductivity can be defined in terms of the heat flow q across a temperature difference.](https://upload.wikimedia.org/wikipedia/commons/a/a3/Simple_definition_of_thermal_conductivity-en.svg)

Consider a solid material placed between two environments of different temperatures. Let $T_1$ be the temperature at $x=0$ and $T_2$ be the temperature at $x=L$, and suppose $T_2 > T_1$. An example of this scenario is a building on a cold winter day; the solid material in this case is the building wall, separating the cold outdoor environment from the warm indoor environment.

According to the [second law of thermodynamics](https://en.wikipedia.org/wiki/Second_law_of_thermodynamics), heat will flow from the hot environment to the cold one as the temperature difference is equalized by diffusion. This is quantified in terms of a [heat flux](https://en.wikipedia.org/wiki/Heat_flux) $q$, which gives the rate, per unit area, at which heat flows in a given direction (in this case minus x-direction). In many materials, $q$ is observed to be directly proportional to the temperature difference and inversely proportional to the separation distance $L$:

$$q = -k \cdot \frac{T_2 - T_1}{L}$$

The constant of proportionality $k$ is the thermal conductivity; it is a physical property of the material. In the present scenario, since $T_2 > T_1$ heat flows in the minus x-direction and $q$ is negative, which in turn means that $k>0$. In general, $k$ is always defined to be positive. The same definition of $k$ can also be extended to gases and liquids, provided other modes of energy transport, such as [convection](https://en.wikipedia.org/wiki/Convection) and [radiation](https://en.wikipedia.org/wiki/Radiative_transfer), are eliminated or accounted for.

The preceding derivation assumes that the $k$ does not change significantly as temperature is varied from $T_1$ to $T_2$. Cases in which the temperature variation of $k$ is non-negligible must be addressed using the more general definition of $k$ discussed below.

### General definition

Thermal conduction is defined as the transport of energy due to random molecular motion across a temperature gradient. It is distinguished from energy transport by convection and molecular work in that it does not involve macroscopic flows or work-performing internal stresses.

Energy flow due to thermal conduction is classified as heat and is quantified by the vector $\mathbf{q}(\mathbf{r}, t)$, which gives the heat flux at position $\mathbf{r}$ and time $t$. According to the second law of thermodynamics, heat flows from high to low temperature. Hence, it is reasonable to postulate that $\mathbf{q}(\mathbf{r}, t)$ is proportional to the gradient of the temperature field $T(\mathbf{r}, t)$, i.e.

$$\mathbf{q}(\mathbf{r}, t) = -k \nabla T(\mathbf{r}, t)$$

where the constant of proportionality, $k > 0$, is the thermal conductivity. This is called Fourier's law of heat conduction. Despite its name, it is not a law but a definition of thermal conductivity in terms of the independent physical quantities $\mathbf{q}(\mathbf{r}, t)$ and $T(\mathbf{r}, t)$. As such, its usefulness depends on the ability to determine $k$ for a given material under given conditions. The constant $k$ itself usually depends on $T(\mathbf{r}, t)$ and thereby implicitly on space and time. An explicit space and time dependence could also occur if the material is inhomogeneous or changing with time.

In some solids, thermal conduction is [anisotropic](https://en.wikipedia.org/wiki/Anisotropic), i.e. the heat flux is not always parallel to the temperature gradient. To account for such behavior, a tensorial form of [Fourier's law](https://en.wikipedia.org/wiki/Fourier%27s_law) must be used:

$$\mathbf{q}(\mathbf{r}, t) = -\boldsymbol{\kappa} \cdot \nabla T(\mathbf{r}, t)$$

where $\boldsymbol{\kappa}$ is symmetric, second-rank [tensor](https://en.wikipedia.org/wiki/Tensor) called the thermal conductivity tensor.

An implicit assumption in the above description is the presence of [local thermodynamic equilibrium](https://en.wikipedia.org/wiki/Local_thermodynamic_equilibrium), which allows one to define a temperature field $T(\mathbf{r}, t)$. This assumption could be violated in systems that are unable to attain local equilibrium, as might happen in the presence of strong nonequilibrium driving or long-ranged interactions.

### Other quantities

In engineering practice, it is common to work in terms of quantities which are derivative to thermal conductivity and implicitly take into account design-specific features such as component dimensions.

For instance, **thermal conductance** is defined as the quantity of heat that passes in unit time through a plate of *particular area and thickness* when its opposite faces differ in temperature by one kelvin. For a plate of thermal conductivity $k$, area $A$ and thickness $L$, the conductance is $kA/L$, measured in W⋅K$^{-1}$. The relationship between thermal conductivity and conductance is analogous to the relationship between [electrical conductivity](https://en.wikipedia.org/wiki/Electrical_conductivity) and [electrical conductance](https://en.wikipedia.org/wiki/Electrical_conductance).

**Thermal resistance** is the inverse of thermal conductance. It is a convenient measure to use in multicomponent design since thermal resistances are additive when occurring in [series](https://en.wikipedia.org/wiki/Series_and_parallel_circuits).

There is also a measure known as the [heat transfer coefficient](https://en.wikipedia.org/wiki/Heat_transfer_coefficient): the quantity of heat that passes per unit time through a unit area of a plate of particular thickness when its opposite faces differ in temperature by one kelvin. In [ASTM](https://en.wikipedia.org/wiki/ASTM) C168-15, this area-independent quantity is referred to as the "thermal conductance". The reciprocal of the heat transfer coefficient is **thermal insulance**. In summary, for a plate of thermal conductivity $k$, area $A$ and thickness $L$,

* thermal conductance = $kA/L$, measured in W⋅K$^{-1}$.
  * thermal resistance = $L/(kA)$, measured in K⋅W$^{-1}$.
* heat transfer coefficient = $k/L$, measured in W⋅K$^{-1}$⋅m$^{-2}$.
  * thermal insulance = $L/k$, measured in K⋅m$^2$⋅W$^{-1}$.

The heat transfer coefficient is also known as **thermal admittance** in the sense that the material may be seen as admitting heat to flow.

An additional term, [thermal transmittance](https://en.wikipedia.org/wiki/Thermal_transmittance), quantifies the thermal conductance of a structure along with heat transfer due to [convection](https://en.wikipedia.org/wiki/Convection) and [radiation](https://en.wikipedia.org/wiki/Thermal_radiation). It is measured in the same units as thermal conductance and is sometimes known as the *composite thermal conductance*. The term *[U-value](https://en.wikipedia.org/wiki/U-value)* is also used.

Finally, [thermal diffusivity](https://en.wikipedia.org/wiki/Thermal_diffusivity) $\alpha$ combines thermal conductivity with [density](https://en.wikipedia.org/wiki/Density) and [specific heat](https://en.wikipedia.org/wiki/Specific_heat):

$$\alpha = \frac{k}{\rho c_{p}}$$

As such, it quantifies the *thermal inertia* of a material, i.e. the relative difficulty in heating a material to a given temperature using heat sources applied at the boundary.

## Units

In the [International System of Units](https://en.wikipedia.org/wiki/International_System_of_Units) (SI), thermal conductivity is measured in [watts](https://en.wikipedia.org/wiki/Watt) per meter-kelvin ([W](https://en.wikipedia.org/wiki/Watt)/([m](https://en.wikipedia.org/wiki/Metre)⋅[K](https://en.wikipedia.org/wiki/Kelvin))). Some papers report in watts per centimeter-kelvin [W/(cm⋅K)].

However, physicists use other convenient units as well, e.g., in [cgs units](https://en.wikipedia.org/wiki/Cgs_units), where esu/(cm-sec-K) is used. The [Lorentz number](https://en.wikipedia.org/wiki/Lorentz_number), defined as L=κ/σT is a quantity independent of the carrier density and the scattering mechanism. Its value for a gas of non-interacting electrons (typical carriers in good metallic conductors) is 2.72×10$^{-13}$ esu/K$^{2}$, or equivalently, 2.44×10$^{-8}$ Watt-Ohm/K$^{2}$.

In [imperial units](https://en.wikipedia.org/wiki/Imperial_units), thermal conductivity is measured in [BTU](https://en.wikipedia.org/wiki/British_thermal_unit)/([h](https://en.wikipedia.org/wiki/Hour)⋅[ft](https://en.wikipedia.org/wiki/Foot_(unit))⋅[°F](https://en.wikipedia.org/wiki/Fahrenheit)).

The [dimension](https://en.wikipedia.org/wiki/Dimensional_analysis) of thermal conductivity is M$^{1}$L$^{1}$T$^{-3}$Θ$^{-1}$, expressed in terms of the dimensions mass (M), length (L), time (T), and temperature (Θ).

Other units which are closely related to the thermal conductivity are in common use in the construction and textile industries. The construction industry makes use of measures such as the [R-value](https://en.wikipedia.org/wiki/R-value_(insulation)) (resistance) and the [U-value](https://en.wikipedia.org/wiki/R-value_(insulation)#U-factor/U-value) (transmittance or conductance). Although related to the thermal conductivity of a material used in an insulation product or assembly, R- and U-values are measured per unit area, and depend on the specified thickness of the product or assembly.

Likewise the textile industry has several units including the [tog](https://en.wikipedia.org/wiki/Tog_(unit)) and the [clo](https://en.wikipedia.org/wiki/Clothing_insulation#Units_and_measurement) which express thermal resistance of a material in a way analogous to the R-values used in the construction industry.

## Measurement

Thermal conductivity measurement methods are described in detail in a separate article: [Thermal conductivity measurement](https://en.wikipedia.org/wiki/Thermal_conductivity_measurement)

There are several ways to measure thermal conductivity; each is suitable for a limited range of materials. Broadly speaking, there are two categories of measurement techniques: *steady-state* and *transient*. Steady-state techniques infer the thermal conductivity from measurements on the state of a material once a steady-state temperature profile has been reached, whereas transient techniques operate on the instantaneous state of a system during the approach to steady state. Lacking an explicit time component, steady-state techniques do not require complicated [signal analysis](https://en.wikipedia.org/wiki/Signal_analysis) (steady state implies constant signals). The disadvantage is that a well-engineered experimental setup is usually needed, and the time required to reach steady state precludes rapid measurement.

In comparison with solid materials, the thermal properties of fluids are more difficult to study experimentally. This is because in addition to thermal conduction, convective and radiative energy transport are usually present unless measures are taken to limit these processes. The formation of an insulating boundary layer can also result in an apparent reduction in the thermal conductivity.

## Experimental values

For a comprehensive list of materials and their thermal conductivity values, see: [List of thermal conductivities](https://en.wikipedia.org/wiki/List_of_thermal_conductivities)

The thermal conductivities of common substances span at least four orders of magnitude. Gases generally have low thermal conductivity, and pure metals have high thermal conductivity. For example, under [standard conditions](https://en.wikipedia.org/wiki/Standard_conditions) the thermal conductivity of [copper](https://en.wikipedia.org/wiki/Copper) is over 10,000 times that of air.

Of all materials, [allotropes](https://en.wikipedia.org/wiki/Allotropes) of carbon, such as [graphite](https://en.wikipedia.org/wiki/Graphite) and [diamond](https://en.wikipedia.org/wiki/Diamond), are usually credited with having the highest thermal conductivities at room temperature. The thermal conductivity of natural diamond at room temperature is several times higher than that of a highly conductive metal such as copper (although the precise value varies depending on the [diamond type](https://en.wikipedia.org/wiki/Diamond_type)).

Thermal conductivities of selected substances are tabulated below; an expanded list can be found in the [list of thermal conductivities](https://en.wikipedia.org/wiki/List_of_thermal_conductivities). These values are illustrative estimates only, as they do not account for measurement uncertainties or variability in material definitions.

| Substance | Thermal conductivity (W·m$^{-1}$·K$^{-1}$) | Temperature (°C) |
|-----------|-------------------------------------------|-----------------|
| [Air](https://en.wikipedia.org/wiki/Air) | 0.026 | 25 |
| [Styrofoam](https://en.wikipedia.org/wiki/Styrofoam) | 0.033 | 25 |
| [Water](https://en.wikipedia.org/wiki/Water) | 0.6089 | 26.85 |
| [Concrete](https://en.wikipedia.org/wiki/Concrete) | 0.92 | – |
| [Steel](https://en.wikipedia.org/wiki/Steel) | 45 | 18.05 |
| [Aluminium](https://en.wikipedia.org/wiki/Aluminium) | 237 | 18.05 |
| [Copper](https://en.wikipedia.org/wiki/Copper) | 384 | 18.05 |
| [Diamond](https://en.wikipedia.org/wiki/Diamond) | 895–1350 | 26.85 |

## Influencing factors

### Temperature

The effect of temperature on thermal conductivity is different for metals and nonmetals. In metals, heat conductivity is primarily due to free electrons. Following the [Wiedemann–Franz law](https://en.wikipedia.org/wiki/Wiedemann–Franz_law), thermal conductivity of metals is approximately proportional to the absolute temperature (in [kelvins](https://en.wikipedia.org/wiki/Kelvin)) times electrical conductivity. In pure metals the electrical conductivity decreases with increasing temperature and thus the product of the two, the thermal conductivity, stays approximately constant. However, as temperatures approach absolute zero, the thermal conductivity decreases sharply.

In alloys the change in electrical conductivity is usually smaller and thus thermal conductivity increases with temperature, often proportionally to temperature. Many pure metals have a peak thermal conductivity between 2 K and 10 K.

On the other hand, heat conductivity in nonmetals is mainly due to lattice vibrations ([phonons](https://en.wikipedia.org/wiki/Phonon)). Except for high-quality crystals at low temperatures, the phonon mean free path is not reduced significantly at higher temperatures. Thus, the thermal conductivity of nonmetals is approximately constant at high temperatures. At low temperatures well below the [Debye temperature](https://en.wikipedia.org/wiki/Debye_model#Debye_temperature_table), thermal conductivity decreases, as does the heat capacity, due to [carrier scattering](https://en.wikipedia.org/wiki/Carrier_scattering) from defects.

### Chemical phase

When a material undergoes a phase change (e.g. from solid to liquid), the thermal conductivity may change abruptly. For instance, when ice melts to form liquid water at 0 °C, the thermal conductivity changes from 2.18 W/(m⋅K) to 0.56 W/(m⋅K).

Even more dramatically, the thermal conductivity of a fluid diverges in the vicinity of the vapor-liquid [critical point](https://en.wikipedia.org/wiki/Critical_phenomena).

### Thermal anisotropy

Some substances, such as non-[cubic](https://en.wikipedia.org/wiki/Cubic_crystal_system) [crystals](https://en.wikipedia.org/wiki/Crystal), can exhibit different thermal conductivities along different crystal axes. [Sapphire](https://en.wikipedia.org/wiki/Sapphire) is a notable example of variable thermal conductivity based on orientation and temperature, with 35 W/(m⋅K) along the *c* axis and 32 W/(m⋅K) along the *a* axis.

[Wood](https://en.wikipedia.org/wiki/Wood) generally conducts better along the grain than across it. Other examples of materials where the thermal conductivity varies with direction are metals that have undergone [cold pressing](https://en.wikipedia.org/wiki/Cold-formed_steel), [laminated](https://en.wikipedia.org/wiki/Lamination) materials, cables, the materials used for the [Space Shuttle thermal protection system](https://en.wikipedia.org/wiki/Space_Shuttle_thermal_protection_system), and [fiber-reinforced composite](https://en.wikipedia.org/wiki/Fiber-reinforced_composite) structures.

When anisotropy is present, the direction of heat flow may differ from the direction of the thermal gradient.

### Electrical conductivity

In metals, thermal conductivity is approximately correlated with electrical conductivity according to the [Wiedemann–Franz law](https://en.wikipedia.org/wiki/Wiedemann–Franz_law), as freely moving [valence electrons](https://en.wikipedia.org/wiki/Valence_electron) transfer not only electric current but also heat energy. However, the general correlation between electrical and thermal conductance does not hold for other materials, due to the increased importance of [phonon](https://en.wikipedia.org/wiki/Phonon) carriers for heat in non-metals. Highly electrically conductive [silver](https://en.wikipedia.org/wiki/Silver) is less thermally conductive than [diamond](https://en.wikipedia.org/wiki/Diamond), which is an [electrical insulator](https://en.wikipedia.org/wiki/Electrical_insulator) but conducts heat via phonons due to its orderly array of atoms.

### Magnetic field

The influence of magnetic fields on thermal conductivity is known as the [thermal Hall effect](https://en.wikipedia.org/wiki/Thermal_Hall_effect) or Righi–Leduc effect.

### Gaseous phases

In the absence of convection, air and other gases are good insulators. Therefore, many insulating materials function simply by having a large number of gas-filled pockets which obstruct heat conduction pathways. Examples of these include expanded and extruded [polystyrene](https://en.wikipedia.org/wiki/Polystyrene) (popularly referred to as "styrofoam") and silica [aerogel](https://en.wikipedia.org/wiki/Aerogel), as well as warm clothes. Natural, biological insulators such as fur and [feathers](https://en.wikipedia.org/wiki/Feather) achieve similar effects by trapping air in pores, pockets, or voids.

Low density gases, such as [hydrogen](https://en.wikipedia.org/wiki/Hydrogen) and [helium](https://en.wikipedia.org/wiki/Helium) typically have high thermal conductivity. Dense gases such as [xenon](https://en.wikipedia.org/wiki/Xenon) and [dichlorodifluoromethane](https://en.wikipedia.org/wiki/Dichlorodifluoromethane) have low thermal conductivity. An exception, [sulfur hexafluoride](https://en.wikipedia.org/wiki/Sulfur_hexafluoride), a dense gas, has a relatively high thermal conductivity due to its high [heat capacity](https://en.wikipedia.org/wiki/Heat_capacity). [Argon](https://en.wikipedia.org/wiki/Argon) and [krypton](https://en.wikipedia.org/wiki/Krypton), gases denser than air, are often used in [insulated glazing](https://en.wikipedia.org/wiki/Insulated_glazing) (double paned windows) to improve their insulation characteristics.

The thermal conductivity through bulk materials in porous or granular form is governed by the type of gas in the gaseous phase, and its pressure. At low pressures, the thermal conductivity of a gaseous phase is reduced, with this behaviour governed by the [Knudsen number](https://en.wikipedia.org/wiki/Knudsen_number), defined as $K_n=l/d$, where $l$ is the [mean free path](https://en.wikipedia.org/wiki/Mean_free_path) of gas molecules and $d$ is the typical gap size of the space filled by the gas. In a granular material $d$ corresponds to the characteristic size of the gaseous phase in the pores or intergranular spaces.

### Isotopic purity

The thermal conductivity of a crystal can depend strongly on isotopic purity, assuming other lattice defects are negligible. A notable example is diamond: at a temperature of around 100 [K](https://en.wikipedia.org/wiki/Kelvin) the thermal conductivity increases from 10,000 [W](https://en.wikipedia.org/wiki/Watt)·[m](https://en.wikipedia.org/wiki/Metre)$^{-1}$·[K](https://en.wikipedia.org/wiki/Kelvin)$^{-1}$ for natural [type IIa diamond](https://en.wikipedia.org/wiki/Diamond_type) (98.9% [$^{12}$C](https://en.wikipedia.org/wiki/Carbon-12)), to 41,000 for 99.9% enriched synthetic diamond. A value of 200,000 is predicted for 99.999% [$^{12}$C](https://en.wikipedia.org/wiki/Carbon-12) at 80 K, assuming an otherwise pure crystal. The thermal conductivity of 99% isotopically enriched cubic boron nitride is ~ 1400 [W](https://en.wikipedia.org/wiki/Watt)·[m](https://en.wikipedia.org/wiki/Metre)$^{-1}$·[K](https://en.wikipedia.org/wiki/Kelvin)$^{-1}$, which is 90% higher than that of natural [boron nitride](https://en.wikipedia.org/wiki/Boron_nitride).

## Molecular origins

The molecular mechanisms of thermal conduction vary among different materials, and in general depend on details of the microscopic structure and molecular interactions. As such, thermal conductivity is difficult to predict from first-principles. Any expressions for thermal conductivity which are exact and general, e.g. the [Green-Kubo relations](https://en.wikipedia.org/wiki/Green-Kubo_relations), are difficult to apply in practice, typically consisting of averages over multiparticle [correlation functions](https://en.wikipedia.org/wiki/Correlation_function_(statistical_mechanics)). A notable exception is a monatomic dilute gas, for which a well-developed theory exists expressing thermal conductivity accurately and explicitly in terms of molecular parameters.

In a gas, thermal conduction is mediated by discrete molecular collisions. In a simplified picture of a solid, thermal conduction occurs by two mechanisms: 1) the migration of free electrons and 2) lattice vibrations ([phonons](https://en.wikipedia.org/wiki/Phonon)). The first mechanism dominates in pure metals and the second in non-metallic solids. In liquids, by contrast, the precise microscopic mechanisms of thermal conduction are poorly understood.

### Gases

In a simplified model of a dilute [monatomic](https://en.wikipedia.org/wiki/Monatomic) gas, molecules are modeled as rigid spheres which are in constant motion, colliding [elastically](https://en.wikipedia.org/wiki/Elastic_collision) with each other and with the walls of their container. Consider such a gas at temperature $T$ and with density $\rho$, [specific heat](https://en.wikipedia.org/wiki/Specific_heat) $c_v$ and [molecular mass](https://en.wikipedia.org/wiki/Molecular_mass) $m$. Under these assumptions, an elementary calculation yields for the thermal conductivity

$$k = \beta \rho \lambda c_v \sqrt{\frac{2k_\text{B} T}{\pi m}}$$

where $\beta$ is a numerical constant of order $1$, $k_\text{B}$ is the [Boltzmann constant](https://en.wikipedia.org/wiki/Boltzmann_constant), and $\lambda$ is the [mean free path](https://en.wikipedia.org/wiki/Mean_free_path), which measures the average distance a molecule travels between collisions. Since $\lambda$ is inversely proportional to density, this equation predicts that thermal conductivity is independent of density for fixed temperature. The explanation is that increasing density increases the number of molecules which carry energy but decreases the average distance $\lambda$ a molecule can travel before transferring its energy to a different molecule: these two effects cancel out. For most gases, this prediction agrees well with experiments at pressures up to about 10 [atmospheres](https://en.wikipedia.org/wiki/Atmosphere_(unit)). At higher densities, the simplifying assumption that energy is only transported by the translational motion of particles no longer holds, and the theory must be modified to account for the transfer of energy across a finite distance at the moment of collision between particles, as well as the locally [non-uniform density](https://en.wikipedia.org/wiki/Radial_distribution_function) in a high density gas. This modification has been carried out, yielding [revised Enskog theory](https://en.wikipedia.org/wiki/Revised_Enskog_theory), which predicts a density dependence of the thermal conductivity in dense gases.

Typically, experiments show a more rapid increase with temperature than $k \propto \sqrt{T}$ (here, $\lambda$ is independent of $T$). This failure of the elementary theory can be traced to the oversimplified "hard sphere" model, which both ignores the "softness" of real molecules, and the attractive forces present between real molecules, such as [dispersion forces](https://en.wikipedia.org/wiki/London_dispersion_force).

To incorporate more complex interparticle interactions, a systematic approach is necessary. One such approach is provided by [Chapman–Enskog theory](https://en.wikipedia.org/wiki/Chapman–Enskog_theory), which derives explicit expressions for thermal conductivity starting from the [Boltzmann equation](https://en.wikipedia.org/wiki/Boltzmann_equation). The Boltzmann equation, in turn, provides a statistical description of a dilute gas for *generic* interparticle interactions. For a monatomic gas, expressions for $k$ derived in this way take the form

$$k = \frac{25}{32} \frac{\sqrt{\pi m k_\text{B} T}}{\pi \sigma^2 \Omega(T)} c_v$$

where $\sigma$ is an effective particle diameter and $\Omega(T)$ is a function of temperature whose explicit form depends on the interparticle interaction law. For rigid elastic spheres, $\Omega(T)$ is independent of $T$ and very close to $1$. More complex interaction laws introduce a weak temperature dependence. The precise nature of the dependence is not always easy to discern, however, as $\Omega(T)$ is defined as a multi-dimensional integral which may not be expressible in terms of elementary functions, but must be evaluated numerically. However, for particles interacting through a [Mie potential](https://en.wikipedia.org/wiki/Mie_potential) (a generalisation of the [Lennard-Jones potential](https://en.wikipedia.org/wiki/Lennard-Jones_potential)) highly accurate correlations for $\Omega(T)$ in terms of [reduced units](https://en.wikipedia.org/wiki/Lennard-Jones_potential#Dimensionless_(reduced_units)) have been developed.

An alternate, equivalent way to present the result is in terms of the gas [viscosity](https://en.wikipedia.org/wiki/Viscosity) $\mu$, which can also be calculated in the Chapman–Enskog approach:

$$k = f \mu c_v$$

where $f$ is a numerical factor which in general depends on the molecular model. For smooth spherically symmetric molecules, however, $f$ is very close to $2.5$, not deviating by more than $1\%$ for a variety of interparticle force laws. Since $k$, $\mu$, and $c_v$ are each well-defined physical quantities which can be measured independent of each other, this expression provides a convenient test of the theory. For monatomic gases, such as the [noble gases](https://en.wikipedia.org/wiki/Noble_gases), the agreement with experiment is fairly good.

For gases whose molecules are not spherically symmetric, the expression $k = f \mu c_v$ still holds. In contrast with spherically symmetric molecules, however, $f$ varies significantly depending on the particular form of the interparticle interactions: this is a result of the energy exchanges between the internal and translational [degrees of freedom](https://en.wikipedia.org/wiki/Degrees_of_freedom_(mechanics)) of the molecules. An explicit treatment of this effect is difficult in the Chapman–Enskog approach. Alternately, the approximate expression $f = (1/4){(9 \gamma - 5)}$ was suggested by [Arnold Eucken](https://en.wikipedia.org/wiki/Arnold_Eucken), where $\gamma$ is the [heat capacity ratio](https://en.wikipedia.org/wiki/Heat_capacity_ratio) of the gas.

The entirety of this section assumes the mean free path $\lambda$ is small compared with macroscopic (system) dimensions. In extremely dilute gases this assumption fails, and thermal conduction is described instead by an apparent thermal conductivity which decreases with density. Ultimately, as the density goes to $0$ the system approaches a [vacuum](https://en.wikipedia.org/wiki/Vacuum), and thermal conduction ceases entirely.

### Liquids

The exact mechanisms of thermal conduction are poorly understood in liquids: there is no molecular picture which is both simple and accurate. An example of a simple but very rough theory is that of [Bridgman](https://en.wikipedia.org/wiki/Percy_Williams_Bridgman), in which a liquid is ascribed a local molecular structure similar to that of a solid, i.e. with molecules located approximately on a lattice. Elementary calculations then lead to the expression

$$k = 3(N_\text{A} / V)^{2/3} k_\text{B} v_\text{s}$$

where $N_\text{A}$ is the [Avogadro constant](https://en.wikipedia.org/wiki/Avogadro_constant), $V$ is the volume of a [mole](https://en.wikipedia.org/wiki/Mole_(unit)) of liquid, and $v_\text{s}$ is the [speed of sound](https://en.wikipedia.org/wiki/Speed_of_sound) in the liquid. This is commonly called *Bridgman's equation*.

### Metals

For **metals at low temperatures** the heat is carried mainly by the free electrons. In this case the mean velocity is the Fermi velocity which is temperature independent. The mean free path is determined by the impurities and the crystal imperfections which are temperature independent as well. So the only temperature-dependent quantity is the heat capacity $c$, which, in this case, is proportional to $T$. So

$$k=k_0\,T \text{ (metal at low temperature)}$$

with $k_0$ a constant. For pure metals, $k_0$ is large, so the thermal conductivity is high. At higher temperatures the mean free path is limited by the phonons, so the thermal conductivity tends to decrease with temperature. In alloys the density of the impurities is very high, so $l$ and, consequently $k$, are small. Therefore, alloys, such as stainless steel, can be used for thermal insulation.

### Lattice waves, phonons, in dielectric solids

Heat transport in both amorphous and crystalline [dielectric](https://en.wikipedia.org/wiki/Dielectric) solids is by way of elastic vibrations of the lattice (i.e., [phonons](https://en.wikipedia.org/wiki/Phonon)). This transport mechanism is theorized to be limited by the elastic scattering of acoustic phonons at lattice defects. This has been confirmed by the experiments of Chang and Jones on commercial glasses and glass ceramics, where the mean free paths were found to be limited by "internal boundary scattering" to length scales of 10$^{-2}$ cm to 10$^{-3}$ cm.

The phonon mean free path has been associated directly with the effective relaxation length for processes without directional correlation. If V$_\text{g}$ is the group velocity of a phonon wave packet, then the relaxation length $l$ is defined as:

$$l=V_\text{g} t$$

where $t$ is the characteristic relaxation time. Since longitudinal waves have a much greater phase velocity than transverse waves, $V_\text{long}$ is much greater than $V_\text{trans}$, and the relaxation length or mean free path of longitudinal phonons will be much greater. Thus, thermal conductivity will be largely determined by the speed of longitudinal phonons.

Regarding the dependence of wave velocity on wavelength or frequency ([dispersion](https://en.wikipedia.org/wiki/Acoustic_dispersion)), low-frequency phonons of long wavelength will be limited in relaxation length by elastic [Rayleigh scattering](https://en.wikipedia.org/wiki/Rayleigh_scattering). This type of light scattering from small particles is proportional to the fourth power of the frequency. For higher frequencies, the power of the frequency will decrease until at highest frequencies scattering is almost frequency independent. Similar arguments were subsequently generalized to many glass forming substances using [Brillouin scattering](https://en.wikipedia.org/wiki/Brillouin_scattering).

Phonons in the acoustical branch dominate the phonon heat conduction as they have greater energy dispersion and therefore a greater distribution of phonon velocities. Additional optical modes could also be caused by the presence of internal structure (i.e., charge or mass) at a lattice point; it is implied that the group velocity of these modes is low and therefore their contribution to the lattice thermal conductivity $\lambda_L$ ($\kappa_L$) is small.

Each phonon mode can be split into one longitudinal and two transverse polarization branches. By extrapolating the phenomenology of lattice points to the unit cells it is seen that the total number of degrees of freedom is 3$pq$ when $p$ is the number of primitive cells with $q$ atoms/unit cell. From these only 3$p$ are associated with the acoustic modes, the remaining 3$p(q - 1)$ are accommodated through the optical branches. This implies that structures with larger $p$ and $q$ contain a greater number of optical modes and a reduced $\lambda_L$.

From these ideas, it can be concluded that increasing crystal complexity, which is described by a complexity factor CF (defined as the number of atoms/primitive unit cell), decreases λ$_L$.

Describing anharmonic effects is complicated because an exact treatment as in the harmonic case is not possible, and phonons are no longer exact eigensolutions to the equations of motion. Even if the state of motion of the crystal could be described with a plane wave at a particular time, its accuracy would deteriorate progressively with time. Time development would have to be described by introducing a spectrum of other phonons, which is known as the phonon decay. The two most important anharmonic effects are the thermal expansion and the phonon thermal conductivity.

Only when the phonon number ‹n› deviates from the equilibrium value ‹n›$^0$, can a thermal current arise as stated in the following expression

$$Q_x=\frac{1}{V} \sum_{q,j} {\hslash \omega \left (\left \langle n \right \rangle-{ \left \langle n \right \rangle}^0 \right)v_x}$$

where $v$ is the energy transport velocity of phonons. Only two mechanisms exist that can cause time variation of ‹$n$› in a particular region. The number of phonons that diffuse into the region from neighboring regions differs from those that diffuse out, or phonons decay inside the same region into other phonons. A special form of the [Boltzmann equation](https://en.wikipedia.org/wiki/Boltzmann_equation)

$$\frac{d\left \langle n\right \rangle}{dt}={\left(\frac{\partial \left \langle n\right \rangle}{\partial t}\right)}_{\text{diff.}}+{\left(\frac{\partial \left \langle n\right \rangle}{\partial t}\right)}_\text{decay}$$

states this. When steady state conditions are assumed the total time derivate of phonon number is zero, because the temperature is constant in time and therefore the phonon number stays also constant. Time variation due to phonon decay is described with a relaxation time ($\tau$) approximation

$${\left(\frac{\partial \left \langle n\right \rangle}{\partial t}\right)}_\text{decay}=-\text{ }\frac{\left \langle n\right \rangle-{\left \langle n\right \rangle}^{0}}{\tau}$$

which states that the more the phonon number deviates from its equilibrium value, the more its time variation increases. At steady state conditions and local thermal equilibrium are assumed we get the following equation

$${\left(\frac{\partial \left(n\right)}{\partial t}\right)}_\text{diff.}=-{v}_{x}\frac{\partial {\left(n\right)}^{0}}{\partial T}\frac{\partial T}{\partial x}$$

Using the relaxation time approximation for the Boltzmann equation and assuming steady-state conditions, the phonon thermal conductivity $\lambda_L$ can be determined. The temperature dependence for $\lambda_L$ originates from the variety of processes, whose significance for $\lambda_L$ depends on the temperature range of interest. Mean free path is one factor that determines the temperature dependence for $\lambda_L$, as stated in the following equation

$${\lambda}_{L}=\frac{1}{3V}\sum _{q,j}v\left(q,j\right)\Lambda \left(q,j\right)\frac{\partial}{\partial T}\epsilon \left(\omega \left(q,j\right),T\right)$$

where Λ is the mean free path for phonon and $\frac{\partial}{\partial T}\epsilon$ denotes the [heat capacity](https://en.wikipedia.org/wiki/Heat_capacity). This equation is a result of combining the four previous equations with each other and knowing that $\left \langle v_x^2\right \rangle=\frac{1}{3}v^2$ for cubic or isotropic systems and $\Lambda =v\tau$.

At low temperatures (< 10 K) the anharmonic interaction does not influence the mean free path and therefore, the thermal resistivity is determined only from processes for which q-conservation does not hold. These processes include the scattering of phonons by crystal defects, or the scattering from the surface of the crystal in case of high quality single crystal. Therefore, thermal conductance depends on the external dimensions of the crystal and the quality of the surface. Thus, temperature dependence of λ$_L$ is determined by the specific heat and is therefore proportional to T$^3$.

Phonon quasimomentum is defined as ℏq and differs from normal momentum because it is only defined within an arbitrary reciprocal lattice vector. At higher temperatures (10 K < $T$ < $\Theta$), the conservation of energy $\hslash {\omega}_{1}=\hslash {\omega}_{2}+\hslash {\omega}_{3}$ and quasimomentum $\mathbf{q}_{1}=\mathbf{q}_{2}+\mathbf{q}_{3}+\mathbf{G}$, where $\mathbf{q}_1$ is wave vector of the incident phonon and $\mathbf{q}_2$, $\mathbf{q}_3$ are wave vectors of the resultant phonons, may also involve a reciprocal lattice vector $\mathbf{G}$ complicating the energy transport process. These processes can also reverse the direction of energy transport.

Therefore, these processes are also known as [Umklapp](https://en.wikipedia.org/wiki/Umklapp_scattering) (U) processes and can only occur when phonons with sufficiently large $q$-vectors are excited, because unless the sum of $\mathbf{q}_2$ and $\mathbf{q}_3$ points outside of the Brillouin zone the momentum is conserved and the process is normal scattering (N-process). The probability of a phonon to have energy $E$ is given by the Boltzmann distribution $P\propto {e}^{-E/kT}$. To U-process to occur the decaying phonon to have a wave vector $\mathbf{q}_1$ that is roughly half of the diameter of the Brillouin zone, because otherwise quasimomentum would not be conserved.

Therefore, these phonons have to possess energy of $\sim k\Theta /2$, which is a significant fraction of Debye energy that is needed to generate new phonons. The probability for this is proportional to ${e}^{-\Theta /bT}$, with $b=2$. Temperature dependence of the mean free path has an exponential form ${e}^{\Theta /bT}$. The presence of the reciprocal lattice wave vector implies a net phonon backscattering and a resistance to phonon and thermal transport resulting finite $\lambda_L$, as it means that momentum is not conserved. Only momentum non-conserving processes can cause thermal resistance.

At high temperatures ($T$ > Θ), the mean free path and therefore $\lambda_L$ has a temperature dependence $T^{-1}$, to which one arrives from formula ${e}^{\Theta /bT}$ by making the following approximation ${e}^{x}\propto x, (x) < 1$ and writing $x=\Theta /bT$. This dependency is known as Eucken's law and originates from the temperature dependency of the probability for the U-process to occur.

Thermal conductivity is usually described by the Boltzmann equation with the relaxation time approximation in which phonon scattering is a limiting factor. Another approach is to use analytic models or molecular dynamics or Monte Carlo based methods to describe thermal conductivity in solids.

Short wavelength phonons are strongly scattered by impurity atoms if an alloyed phase is present, but mid and long wavelength phonons are less affected. Mid and long wavelength phonons carry significant fraction of heat, so to further reduce lattice thermal conductivity one has to introduce structures to scatter these phonons. This is achieved by introducing interface scattering mechanism, which requires structures whose characteristic length is longer than that of impurity atom. Some possible ways to realize these interfaces are nanocomposites and embedded [nanoparticles](https://en.wikipedia.org/wiki/Nanoparticle) or structures.

## Prediction

Because thermal conductivity depends continuously on quantities like temperature and material composition, it cannot be fully characterized by a finite number of experimental measurements. Predictive formulas become necessary if experimental values are not available under the physical conditions of interest. This capability is important in thermophysical simulations, where quantities like temperature and pressure vary continuously with space and time, and may encompass extreme conditions inaccessible to direct measurement.

### In fluids

For the simplest fluids, such as monatomic gases and their mixtures at low to moderate densities, *[ab initio](https://en.wikipedia.org/wiki/Ab_initio)* quantum mechanical computations can accurately predict thermal conductivity in terms of fundamental atomic properties—that is, without reference to existing measurements of thermal conductivity or other transport properties. This method uses [Chapman-Enskog theory](https://en.wikipedia.org/wiki/Chapman–Enskog_theory) or [Revised Enskog Theory](https://en.wikipedia.org/wiki/Revised_Enskog_theory) to evaluate the thermal conductivity, taking fundamental intermolecular potentials as input, which are computed *ab initio* from a quantum mechanical description.

For most fluids, such high-accuracy, first-principles computations are not feasible. Rather, theoretical or empirical expressions must be fit to existing thermal conductivity measurements. If such an expression is fit to high-fidelity data over a large range of temperatures and pressures, then it is called a "reference correlation" for that material. Reference correlations have been published for many pure materials; examples are [carbon dioxide](https://en.wikipedia.org/wiki/Carbon_dioxide), [ammonia](https://en.wikipedia.org/wiki/Ammonia), and [benzene](https://en.wikipedia.org/wiki/Benzene).

Thermophysical modeling software often relies on reference correlations for predicting thermal conductivity at user-specified temperature and pressure. These correlations may be proprietary. Examples are [REFPROP](https://en.wikipedia.org/wiki/REFPROP) (proprietary) and [CoolProp](https://en.wikipedia.org/wiki/CoolProp) (open-source).

Thermal conductivity can also be computed using the [Green-Kubo relations](https://en.wikipedia.org/wiki/Green-Kubo_relations), which express transport coefficients in terms of the statistics of molecular trajectories. The advantage of these expressions is that they are formally exact and valid for general systems. The disadvantage is that they require detailed knowledge of particle trajectories, available only in computationally expensive simulations such as [molecular dynamics](https://en.wikipedia.org/wiki/Molecular_dynamics). An accurate model for interparticle interactions is also required, which may be difficult to obtain for complex molecules.

## History

### Jan Ingenhousz and the thermal conductivity of different metals

In a 1780 letter to [Benjamin Franklin](https://en.wikipedia.org/wiki/Benjamin_Franklin), Dutch-born British scientist [Jan Ingenhousz](https://en.wikipedia.org/wiki/Jan_Ingenhousz) relates an experiment which enabled him to rank seven different metals according to their thermal conductivities:

> You remembre you gave me a wire of five metals all drawn thro the same hole Viz. one, of gould, one of silver, copper steel and iron. I supplyed here the two others Viz. the one of tin the other of lead. I fixed these seven wires into a wooden frame at an equal distance of one an other ... I dipt the seven wires into this melted wax as deep as the wooden frame ... By taking them out they were cov[e]red with a coat of wax ... When I found that this crust was there about of an equal thikness upon all the wires, I placed them all in a glased earthen vessel full of olive oil heated to some degrees under boiling, taking care that each wire was dipt just as far in the oil as the other ... Now, as they had been all dipt alike at the same time in the same oil, it must follow, that the wire, upon which the wax had been melted the highest, had been the best conductor of heat. ... Silver conducted heat far the best of all other metals, next to this was copper, then gold, tin, iron, steel, Lead.

## See also
- [Copper in heat exchangers](https://en.wikipedia.org/wiki/Copper_in_heat_exchangers)
- [Heat pump](https://en.wikipedia.org/wiki/Heat_pump)
- [Heat transfer](https://en.wikipedia.org/wiki/Heat_transfer)
- [Heat transfer mechanisms](https://en.wikipedia.org/wiki/Heat_transfer#Mechanisms)
- [Insulated pipe](https://en.wikipedia.org/wiki/Insulated_pipe)
- [Interfacial thermal resistance](https://en.wikipedia.org/wiki/Interfacial_thermal_resistance)
- [Laser flash analysis](https://en.wikipedia.org/wiki/Laser_flash_analysis)
- [List of thermal conductivities](https://en.wikipedia.org/wiki/List_of_thermal_conductivities)
- [Phase-change material](https://en.wikipedia.org/wiki/Phase-change_material)
- [Physical crystallography before X-rays](https://en.wikipedia.org/wiki/Physical_crystallography_before_X-rays#Thermal_conduction)
- [R-value (insulation)](https://en.wikipedia.org/wiki/R-value_(insulation))
- [Specific heat capacity](https://en.wikipedia.org/wiki/Specific_heat_capacity)
- [Thermal bridge](https://en.wikipedia.org/wiki/Thermal_bridge)
- [Thermal conductance quantum](https://en.wikipedia.org/wiki/Thermal_conductance_quantum)
- [Thermal contact conductance](https://en.wikipedia.org/wiki/Thermal_contact_conductance)
- [Thermal diffusivity](https://en.wikipedia.org/wiki/Thermal_diffusivity)
- [Thermal effusivity](https://en.wikipedia.org/wiki/Thermal_effusivity)
- [Thermal entrance length](https://en.wikipedia.org/wiki/Thermal_entrance_length)
- [Thermal interface material](https://en.wikipedia.org/wiki/Thermal_interface_material)
- [Thermal diode](https://en.wikipedia.org/wiki/Thermal_diode)
- [Thermal resistance](https://en.wikipedia.org/wiki/Thermal_resistance)
- [Thermistor](https://en.wikipedia.org/wiki/Thermistor)
- [Thermocouple](https://en.wikipedia.org/wiki/Thermocouple)
- [Thermodynamics](https://en.wikipedia.org/wiki/Thermodynamics)
- [Thermal conductivity measurement](https://en.wikipedia.org/wiki/Thermal_conductivity_measurement)
- [Refractory metals](https://en.wikipedia.org/wiki/Refractory_metals)

