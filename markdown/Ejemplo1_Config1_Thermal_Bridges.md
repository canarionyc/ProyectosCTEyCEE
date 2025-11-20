
### Revised Thermal Model Including Thermal Bridges

We'll calculate the overall heat transfer coefficient (H_T) for the building envelope, which sums up heat losses through all elements, including thermal bridges.

**H_T = Σ(U_i × A_i) + Σ(Ψ_j × l_j)**
- Where:
  - U_i is the U-value of plane element i (W/m²K)
  - A_i is the area of element i (m²)
  - Ψ_j is the linear thermal transmittance of bridge j (W/mK)
  - l_j is the length of bridge j (m)

### Thermal Bridges to Consider

For our building, the main linear thermal bridges are:

1. **Wall-to-Ceiling Junction (Eaves)**: Where the external wall meets the ceiling of the heated space
2. **Wall-to-Wall Corners**: External corners where two walls meet
3. **Roof Ridge**: Where roof planes meet at the top (though less impactful for uninhabited attic)
4. **Wall-to-Floor Junction**: Where walls meet the ground floor (though we'll focus above-grade)

### Step 1: Calculate Plane Element Heat Losses (from previous analysis)

- **Walls**: U_wall = 0.855 W/m²K, A_walls = 128 m²
  - Q_walls = 0.855 × 128 = 109.44 W/K

- **Ceiling-Roof Assembly**: U_overall = 0.467 W/m²K, A_ceiling = 64 m²
  - Q_ceiling = 0.467 × 64 = 29.89 W/K

**Total Plane Element Loss**: 109.44 + 29.89 = 139.33 W/K

### Step 2: Calculate Thermal Bridge Losses

Using typical Ψ-values from standards like ISO 14683:

#### 1. Wall-to-Ceiling Junction (Eaves)
- **Length**: Perimeter of ceiling = 4 × 8 m = 32 m
- **Ψ-value**: Typical Ψ_eaves = 0.05 W/mK (for well-insulated junction)
- **Heat Loss**: Q_eaves = 0.05 × 32 = 1.6 W/K

#### 2. External Wall Corners
- **Number of corners**: 4
- **Length per corner**: Wall height = 4 m
- **Total length**: 4 × 4 = 16 m
- **Ψ-value**: Typical Ψ_corner = 0.1 W/mK (heat concentrates at external corners)
- **Heat Loss**: Q_corners = 0.1 × 16 = 1.6 W/K

#### 3. Roof Ridge
- **Length**: Summit line of pyramid roof = 4 × (diagonal/2) = 4 × (11.314/2) = 22.63 m
- **Ψ-value**: Typical Ψ_ridge = 0.05 W/mK
- **Heat Loss**: Q_ridge = 0.05 × 22.63 = 1.13 W/K

#### 4. Wall-to-Floor Junction (Perimeter)
- **Length**: Building perimeter = 4 × 9 m = 36 m
- **Ψ-value**: Typical Ψ_floor = 0.1 W/mK
- **Heat Loss**: Q_floor_junction = 0.1 × 36 = 3.6 W/K

**Total Thermal Bridge Loss**: 1.6 + 1.6 + 1.13 + 3.6 = 6.93 W/K

### Step 3: Total Building Heat Loss Coefficient

**H_T = Plane Elements + Thermal Bridges**
- H_T = 139.33 + 6.93 = 146.26 W/K

### Step 4: Calculate Average U-value and Impact Assessment

- **Total Envelope Area**: A_total = A_walls + A_ceiling = 128 + 64 = 192 m²
- **Average U-value**: U_avg = H_T / A_total = 146.26 / 192 = 0.762 W/m²K

### Impact Analysis of Thermal Bridges

| Component | Heat Loss (W/K) | Percentage of Total |
|-----------|-----------------|---------------------|
| Walls | 109.44 | 74.8% |
| Ceiling-Roof | 29.89 | 20.4% |
| Thermal Bridges | 6.93 | 4.7% |
| **Total** | **146.26** | **100%** |

**Key Observations:**

1. **Thermal Bridge Impact**: The thermal bridges add ~5% to the total heat loss in this case. In real buildings with poorer details, this can reach 10-30%.

2. **Most Significant Bridges**: 
   - Wall-to-floor junction contributes the most (3.6 W/K)
   - Wall corners and eaves are equally significant (1.6 W/K each)

3. **Relative to Plane Elements**: 
   - Thermal bridges add about 25% to the ceiling heat loss
   - They add about 6% to the wall heat loss

### Practical Implications

1. **Design Considerations**:
   - Use thermal breaks at wall-to-ceiling junctions
   - Consider insulated corner details
   - Properly insulate the perimeter floor slab

2. **Energy Calculation Accuracy**:
   - Ignoring thermal bridges would underestimate total heat loss by ~5%
   - For heating system sizing, this could lead to undersizing

3. **Code Compliance**:
   - Many energy codes now require accounting for thermal bridges
   - The Ψ-values used should be justified by calculation or testing

This comprehensive approach provides a much more realistic assessment of the building's thermal performance, ensuring accurate energy predictions and proper HVAC system sizing. The method can be extended to include other bridges like window reveals, balcony connections, etc., for even greater accuracy.