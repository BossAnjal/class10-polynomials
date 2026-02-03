import streamlit as st
import sympy as sp
from sympy import symbols, solve, simplify
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(
    page_title="Polynomials Chapter Guide",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #1E40AF;
        border-bottom: 2px solid #1E40AF;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .subsection-header {
        font-size: 1.4rem;
        color: #2563EB;
        margin-top: 1.5rem;
    }
    .important-box {
        background-color: #FEF3C7;
        border-left: 4px solid #F59E0B;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .example-box {
        background-color: #EFF6FF;
        border-left: 4px solid #3B82F6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .question-box {
        background-color: #F0F9FF;
        border: 2px solid #0EA5E9;
        padding: 1.2rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .answer-box {
        background-color: #F0FDF4;
        border: 2px solid #10B981;
        padding: 1.2rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">📚 Polynomials Chapter Guide</h1>', unsafe_allow_html=True)
st.markdown("### Class X Mathematics - Chapter 2: Polynomials")

# Sidebar for navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Select Section:",
    ["Introduction", "Geometrical Meaning of Zeroes", 
     "Zeroes & Coefficients Relationship", "Important Points & Formulas",
     "Practice Questions", "Answer Key", "Interactive Tools"]
)

# Introduction Section
if section == "Introduction":
    st.markdown('<h2 class="section-header">2.1 Introduction to Polynomials</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        A **polynomial** is an algebraic expression consisting of variables and coefficients, 
        involving only the operations of addition, subtraction, multiplication, and non-negative integer exponents.
        
        #### Degree of a Polynomial
        The **degree** of a polynomial is the highest power of the variable in the polynomial.
        
        #### Types of Polynomials
        1. **Linear Polynomial**: Degree 1 (e.g., \(2x - 3\), \(y + \sqrt{2}\))
        2. **Quadratic Polynomial**: Degree 2 (e.g., \(2x^2 + 3x - \frac{2}{5}\), \(y^2 - 2\))
        3. **Cubic Polynomial**: Degree 3 (e.g., \(5x^3 - 4x^2 + x - \sqrt{2}\))
        
        #### What is NOT a Polynomial?
        Expressions like \(\\frac{1}{x-1}\), \(\sqrt{x} + 2\), \( \\frac{1}{x^2 + 2x + 3} \) are **not polynomials**.
        """)
    
    with col2:
        st.markdown('<div class="important-box">', unsafe_allow_html=True)
        st.markdown("**Key Points:**")
        st.markdown("""
        - General form of quadratic polynomial: \(ax^2 + bx + c\), \(a ≠ 0\)
        - General form of cubic polynomial: \(ax^3 + bx^2 + cx + d\), \(a ≠ 0\)
        - The coefficient of the highest degree term cannot be zero
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Examples in a table
    st.markdown("#### Examples of Polynomials")
    
    examples_data = {
        "Polynomial": ["4x + 2", "2y² - 3y + 4", "5x³ - 4x² + x - √2", "7u⁶ - ³⁄₂ u⁴ + 4u² + u - 8"],
        "Variable": ["x", "y", "x", "u"],
        "Degree": [1, 2, 3, 6],
        "Type": ["Linear", "Quadratic", "Cubic", "Degree 6"]
    }
    
    st.table(pd.DataFrame(examples_data))
    
    # Value of a polynomial
    st.markdown("#### Value of a Polynomial at a Point")
    st.markdown(r"""
    If \(p(x)\) is a polynomial in \(x\), and \(k\) is any real number, then the value obtained by replacing \(x\) by \(k\) in \(p(x)\) is called the **value of \(p(x)\) at \(x = k\)**, denoted by \(p(k)\).
    
    **Example**: For \(p(x) = x^2 - 3x - 4\),
    - \(p(2) = 2^2 - 3 \times 2 - 4 = -6\)
    - \(p(-1) = (-1)^2 - 3 \times (-1) - 4 = 0\)
    """)

# Geometrical Meaning Section
elif section == "Geometrical Meaning of Zeroes":
    st.markdown('<h2 class="section-header">2.2 Geometrical Meaning of Zeroes of a Polynomial</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    A real number \(k\) is a **zero** of the polynomial \(p(x)\) if \(p(k) = 0\).
    
    Geometrically, the zeroes of a polynomial are the **x-coordinates** of the points where the graph of \(y = p(x)\) intersects the x-axis.
    """)
    
    # Linear Polynomial
    st.markdown('<h3 class="subsection-header">1. Linear Polynomials</h3>', unsafe_allow_html=True)
    st.markdown(r"""
    For a linear polynomial \(ax + b\) (where \(a ≠ 0\)):
    - Graph: Straight line
    - Intersects x-axis at exactly one point: \(\left(-\frac{b}{a}, 0\right)\)
    - Has exactly one zero: \(x = -\frac{b}{a}\)
    
    **Example**: \(y = 2x + 3\)
    - Zero: \(x = -\frac{3}{2}\)
    - Graph intersects x-axis at \(\left(-\frac{3}{2}, 0\right)\)
    """)
    
    # Plot linear polynomial
    with st.expander("Visualize Linear Polynomial Graph"):
        col1, col2 = st.columns(2)
        with col1:
            a = st.slider("Coefficient a (for ax+b)", -5.0, 5.0, 2.0, 0.5)
            b = st.slider("Constant b (for ax+b)", -10.0, 10.0, 3.0, 0.5)
        
        # Generate plot
        x_vals = np.linspace(-10, 10, 400)
        y_vals = a * x_vals + b
        zero = -b/a if a != 0 else None
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'y = {a}x + {b}')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        if zero is not None:
            ax.plot(zero, 0, 'ro', markersize=8, label=f'Zero at x = {zero:.2f}')
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'Graph of y = {a}x + {b}')
        ax.grid(True, alpha=0.3)
        ax.legend()
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        
        st.pyplot(fig)
    
    # Quadratic Polynomial
    st.markdown('<h3 class="subsection-header">2. Quadratic Polynomials</h3>', unsafe_allow_html=True)
    st.markdown(r"""
    For a quadratic polynomial \(ax^2 + bx + c\) (where \(a ≠ 0\)):
    - Graph: Parabola (opens upward if \(a > 0\), downward if \(a < 0\))
    - Can have:
        1. **Two distinct zeroes**: Graph cuts x-axis at two points
        2. **One zero (equal zeroes)**: Graph touches x-axis at one point
        3. **No zero**: Graph doesn't intersect x-axis
    """)
    
    # Plot quadratic polynomial
    with st.expander("Visualize Quadratic Polynomial Graph"):
        col1, col2, col3 = st.columns(3)
        with col1:
            a_q = st.slider("Coefficient a (for ax²+bx+c)", -3.0, 3.0, 1.0, 0.1)
        with col2:
            b_q = st.slider("Coefficient b (for ax²+bx+c)", -10.0, 10.0, -3.0, 0.5)
        with col3:
            c_q = st.slider("Constant c (for ax²+bx+c)", -10.0, 10.0, -4.0, 0.5)
        
        # Generate plot
        x_vals = np.linspace(-10, 10, 400)
        y_vals = a_q * x_vals**2 + b_q * x_vals + c_q
        
        # Calculate zeroes
        discriminant = b_q**2 - 4*a_q*c_q
        if discriminant >= 0 and a_q != 0:
            zero1 = (-b_q + np.sqrt(discriminant)) / (2*a_q)
            zero2 = (-b_q - np.sqrt(discriminant)) / (2*a_q)
            zeroes = [zero1, zero2]
        else:
            zeroes = []
        
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=f'y = {a_q}x² + {b_q}x + {c_q}')
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        
        for zero in zeroes:
            if -10 <= zero <= 10:
                ax.plot(zero, 0, 'ro', markersize=8)
        
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'Graph of y = {a_q}x² + {b_q}x + {c_q}')
        ax.grid(True, alpha=0.3)
        ax.legend()
        ax.set_xlim(-10, 10)
        ax.set_ylim(-20, 20)
        
        st.pyplot(fig)
        
        # Display zero information
        if a_q != 0:
            if discriminant > 0:
                st.success(f"Two distinct zeroes: x₁ = {zero1:.2f}, x₂ = {zero2:.2f}")
            elif discriminant == 0:
                st.info(f"One repeated zero: x = {zero1:.2f}")
            else:
                st.warning("No real zeroes (graph doesn't intersect x-axis)")
    
    # Cubic Polynomial
    st.markdown('<h3 class="subsection-header">3. Cubic Polynomials</h3>', unsafe_allow_html=True)
    st.markdown(r"""
    For a cubic polynomial \(ax^3 + bx^2 + cx + d\) (where \(a ≠ 0\)):
    - Graph: Cubic curve
    - Can have at most 3 zeroes
    - The graph of \(y = p(x)\) intersects the x-axis at at most 3 points
    """)
    
    st.markdown("""
    #### General Observation:
    For a polynomial of degree \(n\):
    - The graph of \(y = p(x)\) intersects the x-axis at at most \(n\) points
    - Therefore, a polynomial of degree \(n\) has at most \(n\) zeroes
    """)

# Zeroes & Coefficients Relationship Section
elif section == "Zeroes & Coefficients Relationship":
    st.markdown('<h2 class="section-header">2.3 Relationship Between Zeroes and Coefficients</h2>', unsafe_allow_html=True)
    
    # Linear Polynomial
    st.markdown('<h3 class="subsection-header">1. Linear Polynomials</h3>', unsafe_allow_html=True)
    st.markdown(r"""
    For a linear polynomial \(p(x) = ax + b\) (where \(a ≠ 0\)):
    
    - Zero: \(x = -\frac{b}{a}\)
    - Relationship: \(\text{Zero} = \frac{-\text{Constant term}}{\text{Coefficient of } x}\)
    """)
    
    # Quadratic Polynomial
    st.markdown('<h3 class="subsection-header">2. Quadratic Polynomials</h3>', unsafe_allow_html=True)
    st.markdown(r"""
    For a quadratic polynomial \(p(x) = ax^2 + bx + c\) (where \(a ≠ 0\)) with zeroes \(\alpha\) and \(\beta\):
    
    **Sum of zeroes**: \(\alpha + \beta = -\frac{b}{a}\)
    
    **Product of zeroes**: \(\alpha\beta = \frac{c}{a}\)
    """)
    
    st.markdown('<div class="example-box">', unsafe_allow_html=True)
    st.markdown("#### Example 1:")
    st.markdown(r"""
    For \(p(x) = 2x^2 - 8x + 6\):
    - Zeroes: \(x = 1\) and \(x = 3\)
    - Sum: \(1 + 3 = 4 = \frac{-(-8)}{2} = -\frac{b}{a}\)
    - Product: \(1 \times 3 = 3 = \frac{6}{2} = \frac{c}{a}\)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Cubic Polynomial
    st.markdown('<h3 class="subsection-header">3. Cubic Polynomials</h3>', unsafe_allow_html=True)
    st.markdown(r"""
    For a cubic polynomial \(p(x) = ax^3 + bx^2 + cx + d\) (where \(a ≠ 0\)) with zeroes \(\alpha\), \(\beta\), and \(\gamma\):
    
    **Sum of zeroes**: \(\alpha + \beta + \gamma = -\frac{b}{a}\)
    
    **Sum of products taken two at a time**: \(\alpha\beta + \beta\gamma + \gamma\alpha = \frac{c}{a}\)
    
    **Product of zeroes**: \(\alpha\beta\gamma = -\frac{d}{a}\)
    """)
    
    st.markdown('<div class="example-box">', unsafe_allow_html=True)
    st.markdown("#### Example 2:")
    st.markdown(r"""
    For \(p(x) = 2x^3 - 5x^2 - 14x + 8\):
    - Zeroes: \(4, -2, \frac{1}{2}\)
    - Sum: \(4 + (-2) + \frac{1}{2} = \frac{5}{2} = \frac{-(-5)}{2} = -\frac{b}{a}\)
    - Sum of products taken two at a time: 
      \(4 \times (-2) + (-2) \times \frac{1}{2} + \frac{1}{2} \times 4 = -8 -1 + 2 = -7 = \frac{-14}{2} = \frac{c}{a}\)
    - Product: \(4 \times (-2) \times \frac{1}{2} = -4 = \frac{-8}{2} = -\frac{d}{a}\)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Interactive calculator
    st.markdown('<div class="important-box">', unsafe_allow_html=True)
    st.markdown("#### Interactive Zero Calculator")
    
    poly_type = st.selectbox("Select polynomial type:", ["Linear", "Quadratic", "Cubic"])
    
    if poly_type == "Linear":
        col1, col2 = st.columns(2)
        with col1:
            a = st.number_input("Enter coefficient a:", value=2.0, format="%.2f")
        with col2:
            b = st.number_input("Enter constant b:", value=3.0, format="%.2f")
        
        if a != 0:
            zero = -b/a
            st.success(f"Zero of {a}x + {b} is: x = {zero:.2f}")
        else:
            st.error("Coefficient a cannot be zero for a linear polynomial!")
    
    elif poly_type == "Quadratic":
        col1, col2, col3 = st.columns(3)
        with col1:
            a = st.number_input("Enter coefficient a:", value=1.0, format="%.2f")
        with col2:
            b = st.number_input("Enter coefficient b:", value=-3.0, format="%.2f")
        with col3:
            c = st.number_input("Enter constant c:", value=-4.0, format="%.2f")
        
        if a != 0:
            discriminant = b**2 - 4*a*c
            
            if discriminant > 0:
                zero1 = (-b + np.sqrt(discriminant)) / (2*a)
                zero2 = (-b - np.sqrt(discriminant)) / (2*a)
                st.success(f"Two distinct zeroes: x₁ = {zero1:.2f}, x₂ = {zero2:.2f}")
                
                # Calculate sum and product
                sum_zeros = zero1 + zero2
                product_zeros = zero1 * zero2
                st.info(f"Sum of zeroes = {sum_zeros:.2f} (Should equal -b/a = {-b/a:.2f})")
                st.info(f"Product of zeroes = {product_zeros:.2f} (Should equal c/a = {c/a:.2f})")
                
            elif discriminant == 0:
                zero = -b/(2*a)
                st.success(f"One repeated zero: x = {zero:.2f}")
                st.info(f"Sum of zeroes = {2*zero:.2f} (Should equal -b/a = {-b/a:.2f})")
                st.info(f"Product of zeroes = {zero**2:.2f} (Should equal c/a = {c/a:.2f})")
                
            else:
                st.warning("No real zeroes (discriminant < 0)")
        else:
            st.error("Coefficient a cannot be zero for a quadratic polynomial!")
    
    else:  # Cubic
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            a = st.number_input("Enter coefficient a:", value=2.0, format="%.2f", key="cubic_a")
        with col2:
            b = st.number_input("Enter coefficient b:", value=-5.0, format="%.2f", key="cubic_b")
        with col3:
            c = st.number_input("Enter coefficient c:", value=-14.0, format="%.2f", key="cubic_c")
        with col4:
            d = st.number_input("Enter constant d:", value=8.0, format="%.2f", key="cubic_d")
        
        if a != 0:
            # Use numpy to find approximate roots for cubic
            coeffs = [a, b, c, d]
            roots = np.roots(coeffs)
            real_roots = [root.real for root in roots if abs(root.imag) < 1e-10]
            
            if real_roots:
                if len(real_roots) == 3:
                    zero1, zero2, zero3 = real_roots
                    st.success(f"Three zeroes: x₁ = {zero1:.2f}, x₂ = {zero2:.2f}, x₃ = {zero3:.2f}")
                    
                    # Calculate relationships
                    sum_zeros = zero1 + zero2 + zero3
                    sum_pairwise = zero1*zero2 + zero2*zero3 + zero3*zero1
                    product_zeros = zero1 * zero2 * zero3
                    
                    st.info(f"Sum of zeroes = {sum_zeros:.2f} (Should equal -b/a = {-b/a:.2f})")
                    st.info(f"Sum of products taken two at a time = {sum_pairwise:.2f} (Should equal c/a = {c/a:.2f})")
                    st.info(f"Product of zeroes = {product_zeros:.2f} (Should equal -d/a = {-d/a:.2f})")
                    
                elif len(real_roots) == 2:
                    # One is repeated
                    st.success(f"Two zeroes (one repeated): x₁ = {real_roots[0]:.2f}, x₂ = {real_roots[1]:.2f}")
                else:
                    st.success(f"One zero: x = {real_roots[0]:.2f}")
            else:
                st.warning("No real zeroes found")
        else:
            st.error("Coefficient a cannot be zero for a cubic polynomial!")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Important Points & Formulas Section
elif section == "Important Points & Formulas":
    st.markdown('<h2 class="section-header">Important Points & Formulas</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="important-box">', unsafe_allow_html=True)
        st.markdown("### Key Definitions")
        st.markdown("""
        1. **Polynomial**: Algebraic expression with non-negative integer exponents
        2. **Degree**: Highest power of the variable
        3. **Zero/Root**: Value of x for which p(x) = 0
        4. **Linear Polynomial**: Degree 1, form: ax + b
        5. **Quadratic Polynomial**: Degree 2, form: ax² + bx + c
        6. **Cubic Polynomial**: Degree 3, form: ax³ + bx² + cx + d
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="important-box">', unsafe_allow_html=True)
        st.markdown("### Maximum Number of Zeroes")
        st.markdown("""
        - Polynomial of degree n has at most n zeroes
        - Linear: At most 1 zero
        - Quadratic: At most 2 zeroes
        - Cubic: At most 3 zeroes
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="important-box">', unsafe_allow_html=True)
        st.markdown("### Relationship Formulas")
        st.markdown("""
        #### Quadratic Polynomial (ax² + bx + c)
        - Sum of zeroes (α + β) = -b/a
        - Product of zeroes (αβ) = c/a
        
        #### Cubic Polynomial (ax³ + bx² + cx + d)
        - Sum of zeroes (α + β + γ) = -b/a
        - Sum of products taken two at a time (αβ + βγ + γα) = c/a
        - Product of zeroes (αβγ) = -d/a
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="important-box">', unsafe_allow_html=True)
        st.markdown("### Geometrical Interpretation")
        st.markdown("""
        - Zeroes are x-coordinates where graph intersects x-axis
        - Linear: Straight line intersecting x-axis at one point
        - Quadratic: Parabola intersecting x-axis at 0, 1, or 2 points
        - Cubic: Cubic curve intersecting x-axis at up to 3 points
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional important points
    st.markdown("---")
    st.markdown("### Common Mistakes to Avoid")
    
    mistake_col1, mistake_col2 = st.columns(2)
    
    with mistake_col1:
        st.markdown("""
        ❌ **Assuming all expressions are polynomials**
        - \(\\frac{1}{x-1}\) is NOT a polynomial
        - \(\sqrt{x} + 2\) is NOT a polynomial
        - \(x^{-2} + 3x\) is NOT a polynomial
        
        ❌ **Forgetting \(a ≠ 0\) condition**
        - For ax² + bx + c, a must be non-zero
        - For ax³ + bx² + cx + d, a must be non-zero
        """)
    
    with mistake_col2:
        st.markdown("""
        ❌ **Confusing degree with number of terms**
        - Degree depends on highest power, not number of terms
        - \(x^5 + 1\) has degree 5 (even with only 2 terms)
        
        ❌ **Incorrectly applying relationship formulas**
        - For quadratic: Sum = -b/a, NOT b/a
        - For cubic: Product = -d/a, NOT d/a
        """)

# Practice Questions Section
elif section == "Practice Questions":
    st.markdown('<h2 class="section-header">Practice Questions</h2>', unsafe_allow_html=True)
    
    st.markdown("### Exercise 1: Find Zeroes and Verify Relationships")
    
    questions = [
        {
            "text": "1. Find the zeroes of the polynomial \(x^2 - 2x - 8\) and verify the relationship between zeroes and coefficients.",
            "type": "quadratic"
        },
        {
            "text": "2. Find the zeroes of \(4s^2 - 4s + 1\) and verify the relationship.",
            "type": "quadratic"
        },
        {
            "text": "3. Find the zeroes of \(6x^2 - 3 - 7x\) and verify the relationship.",
            "type": "quadratic"
        },
        {
            "text": "4. Find the zeroes of \(4u^2 + 8u\) and verify the relationship.",
            "type": "quadratic"
        },
        {
            "text": "5. Find the zeroes of \(t^2 - 15\) and verify the relationship.",
            "type": "quadratic"
        },
        {
            "text": "6. Find the zeroes of \(3x^2 - x - 4\) and verify the relationship.",
            "type": "quadratic"
        }
    ]
    
    for i, q in enumerate(questions):
        st.markdown(f'<div class="question-box">', unsafe_allow_html=True)
        st.markdown(f"**Q{i+1}:** {q['text']}")
        
        with st.expander(f"Show/Hide Solution for Q{i+1}"):
            if i == 0:  # x² - 2x - 8
                st.markdown(r"""
                **Solution:**
                - Factorize: \(x^2 - 2x - 8 = (x - 4)(x + 2)\)
                - Zeroes: \(x = 4\) and \(x = -2\)
                - Sum: \(4 + (-2) = 2 = \frac{-(-2)}{1} = -\frac{b}{a}\)
                - Product: \(4 \times (-2) = -8 = \frac{-8}{1} = \frac{c}{a}\)
                """)
            elif i == 1:  # 4s² - 4s + 1
                st.markdown(r"""
                **Solution:**
                - Factorize: \(4s^2 - 4s + 1 = (2s - 1)^2\)
                - Zeroes: \(s = \frac{1}{2}\) (repeated)
                - Sum: \(\frac{1}{2} + \frac{1}{2} = 1 = \frac{-(-4)}{4} = -\frac{b}{a}\)
                - Product: \(\frac{1}{2} \times \frac{1}{2} = \frac{1}{4} = \frac{1}{4} = \frac{c}{a}\)
                """)
            elif i == 2:  # 6x² - 3 - 7x
                st.markdown(r"""
                **Solution:**
                - Rewrite: \(6x^2 - 7x - 3\)
                - Factorize: \(6x^2 - 7x - 3 = (3x + 1)(2x - 3)\)
                - Zeroes: \(x = -\frac{1}{3}\) and \(x = \frac{3}{2}\)
                - Sum: \(-\frac{1}{3} + \frac{3}{2} = \frac{7}{6} = \frac{-(-7)}{6} = -\frac{b}{a}\)
                - Product: \(-\frac{1}{3} \times \frac{3}{2} = -\frac{1}{2} = \frac{-3}{6} = \frac{c}{a}\)
                """)
            elif i == 3:  # 4u² + 8u
                st.markdown(r"""
                **Solution:**
                - Factorize: \(4u^2 + 8u = 4u(u + 2)\)
                - Zeroes: \(u = 0\) and \(u = -2\)
                - Sum: \(0 + (-2) = -2 = \frac{-8}{4} = -\frac{b}{a}\)
                - Product: \(0 \times (-2) = 0 = \frac{0}{4} = \frac{c}{a}\)
                """)
            elif i == 4:  # t² - 15
                st.markdown(r"""
                **Solution:**
                - Factorize: \(t^2 - 15 = (t - \sqrt{15})(t + \sqrt{15})\)
                - Zeroes: \(t = \sqrt{15}\) and \(t = -\sqrt{15}\)
                - Sum: \(\sqrt{15} + (-\sqrt{15}) = 0 = \frac{-0}{1} = -\frac{b}{a}\)
                - Product: \(\sqrt{15} \times (-\sqrt{15}) = -15 = \frac{-15}{1} = \frac{c}{a}\)
                """)
            elif i == 5:  # 3x² - x - 4
                st.markdown(r"""
                **Solution:**
                - Factorize: \(3x^2 - x - 4 = (3x - 4)(x + 1)\)
                - Zeroes: \(x = \frac{4}{3}\) and \(x = -1\)
                - Sum: \(\frac{4}{3} + (-1) = \frac{1}{3} = \frac{-(-1)}{3} = -\frac{b}{a}\)
                - Product: \(\frac{4}{3} \times (-1) = -\frac{4}{3} = \frac{-4}{3} = \frac{c}{a}\)
                """)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Exercise 2: Find Quadratic Polynomials")
    
    st.markdown('<div class="question-box">', unsafe_allow_html=True)
    st.markdown("Find quadratic polynomials with the following sums and products of zeroes:")
    
    poly_questions = [
        ("(i) Sum = \(\\frac{1}{4}\), Product = -1", "\(4x^2 - x - 4\)"),
        ("(ii) Sum = \(\sqrt{2}\), Product = \(\\frac{1}{3}\)", "\(3x^2 - 3\sqrt{2}x + 1\)"),
        ("(iii) Sum = 0, Product = \(\sqrt{5}\)", "\(x^2 + \sqrt{5}\)"),
        ("(iv) Sum = 1, Product = 1", "\(x^2 - x + 1\)"),
        ("(v) Sum = \(-\\frac{1}{4}\), Product = \(\\frac{1}{4}\)", "\(4x^2 + x + 1\)"),
        ("(vi) Sum = 4, Product = 1", "\(x^2 - 4x + 1\)")
    ]
    
    for q_text, _ in poly_questions:
        st.markdown(f"**{q_text}**")
    
    with st.expander("Show Solutions"):
        for q_text, solution in poly_questions:
            st.markdown(f"**{q_text.split(')')[0]})** Solution: {solution}")
            st.markdown("---")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Answer Key Section
elif section == "Answer Key":
    st.markdown('<h2 class="section-header">Answer Key</h2>', unsafe_allow_html=True)
    
    st.markdown("### Exercise 1 Answers")
    
    answers_ex1 = [
        ("1. \(x^2 - 2x - 8\)", "Zeroes: 4, -2; Sum: 2; Product: -8"),
        ("2. \(4s^2 - 4s + 1\)", "Zeroes: \(\\frac{1}{2}, \\frac{1}{2}\); Sum: 1; Product: \(\\frac{1}{4}\)"),
        ("3. \(6x^2 - 3 - 7x\)", "Zeroes: \(-\\frac{1}{3}, \\frac{3}{2}\); Sum: \(\\frac{7}{6}\); Product: \(-\\frac{1}{2}\)"),
        ("4. \(4u^2 + 8u\)", "Zeroes: 0, -2; Sum: -2; Product: 0"),
        ("5. \(t^2 - 15\)", "Zeroes: \(\sqrt{15}, -\sqrt{15}\); Sum: 0; Product: -15"),
        ("6. \(3x^2 - x - 4\)", "Zeroes: \(\\frac{4}{3}, -1\); Sum: \(\\frac{1}{3}\); Product: \(-\\frac{4}{3}\)")
    ]
    
    for question, answer in answers_ex1:
        st.markdown(f'<div class="answer-box">', unsafe_allow_html=True)
        st.markdown(f"**{question}**")
        st.markdown(f"{answer}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Exercise 2 Answers")
    
    st.markdown("""
    **General Form**: For sum = S and product = P, quadratic polynomial is: \(x^2 - Sx + P\)
    
    (Multiply by constant k if needed to clear fractions)
    """)
    
    answers_ex2 = [
        ("(i) Sum = \(\\frac{1}{4}\), Product = -1", "\(x^2 - \\frac{1}{4}x - 1\) or \(4x^2 - x - 4\)"),
        ("(ii) Sum = \(\sqrt{2}\), Product = \(\\frac{1}{3}\)", "\(x^2 - \sqrt{2}x + \\frac{1}{3}\) or \(3x^2 - 3\sqrt{2}x + 1\)"),
        ("(iii) Sum = 0, Product = \(\sqrt{5}\)", "\(x^2 + \sqrt{5}\)"),
        ("(iv) Sum = 1, Product = 1", "\(x^2 - x + 1\)"),
        ("(v) Sum = \(-\\frac{1}{4}\), Product = \(\\frac{1}{4}\)", "\(x^2 + \\frac{1}{4}x + \\frac{1}{4}\) or \(4x^2 + x + 1\)"),
        ("(vi) Sum = 4, Product = 1", "\(x^2 - 4x + 1\)")
    ]
    
    for question, answer in answers_ex2:
        st.markdown(f'<div class="answer-box">', unsafe_allow_html=True)
        st.markdown(f"**{question}**")
        st.markdown(f"{answer}")
        st.markdown('</div>', unsafe_allow_html=True)

# Interactive Tools Section
else:  # Interactive Tools
    st.markdown('<h2 class="section-header">Interactive Tools</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Polynomial Analyzer", "Graph Plotter", "Zero Finder"])
    
    with tab1:
        st.markdown("### Polynomial Analyzer")
        st.markdown("Enter any polynomial to analyze its properties:")
        
        poly_input = st.text_input("Enter polynomial (use x as variable):", "x^2 - 3x - 4")
        
        if poly_input:
            try:
                x = sp.symbols('x')
                poly_expr = sp.sympify(poly_input)
                
                # Get degree
                degree = sp.Poly(poly_expr, x).degree()
                
                # Get coefficients
                coeffs = sp.Poly(poly_expr, x).all_coeffs()
                
                st.success(f"**Degree:** {degree}")
                
                if degree == 1:
                    st.info("**Type:** Linear Polynomial")
                    a, b = coeffs
                    st.info(f"**Standard Form:** {a}x + {b}")
                    if a != 0:
                        zero = -b/a
                        st.info(f"**Zero:** x = {zero}")
                
                elif degree == 2:
                    st.info("**Type:** Quadratic Polynomial")
                    a, b, c = coeffs
                    st.info(f"**Standard Form:** {a}x² + {b}x + {c}")
                    
                    if a != 0:
                        # Calculate discriminant
                        D = b**2 - 4*a*c
                        st.info(f"**Discriminant:** D = {D}")
                        
                        if D > 0:
                            zero1 = (-b + sp.sqrt(D)) / (2*a)
                            zero2 = (-b - sp.sqrt(D)) / (2*a)
                            st.info(f"**Zeroes:** x₁ = {zero1}, x₂ = {zero2}")
                            st.info(f"**Sum of zeroes:** α + β = {zero1 + zero2} = -b/a = {-b/a}")
                            st.info(f"**Product of zeroes:** αβ = {zero1 * zero2} = c/a = {c/a}")
                        elif D == 0:
                            zero = -b/(2*a)
                            st.info(f"**Zero:** x = {zero} (repeated)")
                            st.info(f"**Sum of zeroes:** α + β = {2*zero} = -b/a = {-b/a}")
                            st.info(f"**Product of zeroes:** αβ = {zero**2} = c/a = {c/a}")
                        else:
                            st.info("**Zeroes:** No real zeroes (complex conjugate pair)")
                
                elif degree == 3:
                    st.info("**Type:** Cubic Polynomial")
                    a, b, c, d = coeffs
                    st.info(f"**Standard Form:** {a}x³ + {b}x² + {c}x + {d}")
                    
                    # Try to find zeroes
                    try:
                        zeroes = sp.solve(poly_expr, x)
                        real_zeroes = [z for z in zeroes if z.is_real]
                        
                        if len(real_zeroes) >= 1:
                            st.info(f"**Real Zeroes:** {real_zeroes}")
                            
                            if len(real_zeroes) == 3:
                                alpha, beta, gamma = real_zeroes
                                st.info(f"**Sum of zeroes:** α + β + γ = {alpha + beta + gamma} = -b/a = {-b/a}")
                                st.info(f"**Sum of products taken two at a time:** αβ + βγ + γα = {alpha*beta + beta*gamma + gamma*alpha} = c/a = {c/a}")
                                st.info(f"**Product of zeroes:** αβγ = {alpha*beta*gamma} = -d/a = {-d/a}")
                        else:
                            st.info("**Zeroes:** No real zeroes found")
                    except:
                        st.warning("Could not find exact zeroes symbolically")
                
                else:
                    st.info(f"**Type:** Polynomial of degree {degree}")
                    st.info(f"**Coefficients:** {coeffs}")
                    
            except Exception as e:
                st.error(f"Error parsing polynomial: {e}")
    
    with tab2:
        st.markdown("### Polynomial Graph Plotter")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            poly_type = st.selectbox("Select polynomial type:", 
                                     ["Linear (ax+b)", "Quadratic (ax²+bx+c)", "Cubic (ax³+bx²+cx+d)"])
            
            if poly_type == "Linear (ax+b)":
                a = st.slider("a", -5.0, 5.0, 2.0, 0.1)
                b = st.slider("b", -10.0, 10.0, 3.0, 0.1)
                x_vals = np.linspace(-10, 10, 400)
                y_vals = a * x_vals + b
                title = f"y = {a}x + {b}"
                
            elif poly_type == "Quadratic (ax²+bx+c)":
                a = st.slider("a", -3.0, 3.0, 1.0, 0.1, key="quad_a")
                b = st.slider("b", -10.0, 10.0, -3.0, 0.1, key="quad_b")
                c = st.slider("c", -10.0, 10.0, -4.0, 0.1, key="quad_c")
                x_vals = np.linspace(-10, 10, 400)
                y_vals = a * x_vals**2 + b * x_vals + c
                title = f"y = {a}x² + {b}x + {c}"
                
            else:  # Cubic
                a = st.slider("a", -2.0, 2.0, 1.0, 0.1, key="cubic_a_plot")
                b = st.slider("b", -5.0, 5.0, 0.0, 0.1, key="cubic_b_plot")
                c = st.slider("c", -5.0, 5.0, -4.0, 0.1, key="cubic_c_plot")
                d = st.slider("d", -10.0, 10.0, 0.0, 0.1, key="cubic_d_plot")
                x_vals = np.linspace(-10, 10, 400)
                y_vals = a * x_vals**3 + b * x_vals**2 + c * x_vals + d
                title = f"y = {a}x³ + {b}x² + {c}x + {d}"
            
            # Find zeroes for plotting
            zeroes = []
            if poly_type == "Linear (ax+b)" and a != 0:
                zeroes.append(-b/a)
            elif poly_type == "Quadratic (ax²+bx+c)" and a != 0:
                discriminant = b**2 - 4*a*c
                if discriminant >= 0:
                    zero1 = (-b + np.sqrt(discriminant)) / (2*a)
                    zero2 = (-b - np.sqrt(discriminant)) / (2*a)
                    zeroes.extend([zero1, zero2])
        
        with col2:
            # Create plot
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x_vals, y_vals, 'b-', linewidth=2, label=title)
            ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
            ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
            
            # Plot zeroes
            for zero in zeroes:
                if -10 <= zero <= 10:
                    ax.plot(zero, 0, 'ro', markersize=8, label=f'Zero at x = {zero:.2f}')
            
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('y', fontsize=12)
            ax.set_title(f'Graph of {title}', fontsize=14)
            ax.grid(True, alpha=0.3)
            ax.legend()
            ax.set_xlim(-10, 10)
            
            # Adjust y-lim based on polynomial type
            if poly_type == "Linear (ax+b)":
                ax.set_ylim(-10, 10)
            elif poly_type == "Quadratic (ax²+bx+c)":
                ax.set_ylim(min(-10, np.min(y_vals)), max(10, np.max(y_vals)))
            else:  # Cubic
                ax.set_ylim(min(-20, np.min(y_vals)), max(20, np.max(y_vals)))
            
            st.pyplot(fig)
    
    with tab3:
        st.markdown("### Zero Finder Tool")
        st.markdown("Find zeroes of any polynomial up to degree 3:")
        
        poly_input2 = st.text_input("Enter polynomial:", "x^2 + 7x + 10", key="zero_finder")
        
        if poly_input2:
            try:
                x = sp.symbols('x')
                poly_expr = sp.sympify(poly_input2)
                degree = sp.Poly(poly_expr, x).degree()
                
                if degree <= 3:
                    # Try to find zeroes symbolically
                    zeroes = sp.solve(poly_expr, x)
                    
                    st.success(f"**Polynomial:** {poly_expr}")
                    st.success(f"**Degree:** {degree}")
                    
                    if zeroes:
                        st.success(f"**Zeroes found:** {zeroes}")
                        
                        # Verify they are zeroes
                        st.info("**Verification:**")
                        for zero in zeroes:
                            value = poly_expr.subs(x, zero)
                            st.info(f"p({zero}) = {value}")
                        
                        # Show relationships if applicable
                        coeffs = sp.Poly(poly_expr, x).all_coeffs()
                        
                        if degree == 2 and len(zeroes) == 2:
                            a, b, c = coeffs
                            alpha, beta = zeroes
                            st.info(f"**Sum of zeroes:** {alpha} + {beta} = {alpha + beta}")
                            st.info(f"**-b/a =** -({b})/({a}) = {-b/a}")
                            st.info(f"**Product of zeroes:** {alpha} × {beta} = {alpha * beta}")
                            st.info(f"**c/a =** {c}/{a} = {c/a}")
                        
                        elif degree == 3 and len(zeroes) == 3:
                            a, b, c, d = coeffs
                            alpha, beta, gamma = zeroes
                            st.info(f"**Sum of zeroes:** {alpha} + {beta} + {gamma} = {alpha + beta + gamma}")
                            st.info(f"**-b/a =** -({b})/({a}) = {-b/a}")
                            st.info(f"**Sum of products (two at a time):** {alpha*beta + beta*gamma + gamma*alpha}")
                            st.info(f"**c/a =** {c}/{a} = {c/a}")
                            st.info(f"**Product of zeroes:** {alpha} × {beta} × {gamma} = {alpha * beta * gamma}")
                            st.info(f"**-d/a =** -({d})/({a}) = {-d/a}")
                    
                    else:
                        st.warning("No zeroes found symbolically. The polynomial may have no real zeroes.")
                
                else:
                    st.warning("This tool supports polynomials up to degree 3 only.")
            
            except Exception as e:
                st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
    <p>Polynomials Chapter Guide • Based on NCERT Class X Mathematics • Created with Streamlit</p>
    <p>Use this app as a comprehensive guide to understand polynomials, their zeroes, and the relationship with coefficients.</p>
</div>
""", unsafe_allow_html=True)
