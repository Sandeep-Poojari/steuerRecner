import plotly.graph_objects as go
import numpy as np
import taxCaclulator as tc


class TaxPlot:

    def plot_tax_summary(start_salary, end_salary, step, severance_pay, assessment_year, joint_filing):
        # Create salary range
        salaries = np.arange(start_salary, end_salary, step)

        salary = []
        taxes = []
        tax_wo_fifth = []
        tax_only_sev = []
        net_incomes = []

        for salary in salaries:
            calculator = tc.TaxCalculator(salary=salary, severance_pay=severance_pay, assessment_year=assessment_year, joint_filing=joint_filing)
            taxes.append(calculator.get_total_tax())
            tax_wo_fifth.append(calculator.get_total_tax_wo_fifth())
            tax_only_sev.append(calculator.get_tax_severance_only())
            net_incomes.append(calculator.get_net_income())


        # Plotly Figure
        fig = go.Figure()

        # Add lines using a helper function
        add_trace = lambda y_values, name, color: fig.add_trace(
            go.Scatter(
                x=salaries,
                y=y_values,
                mode='lines',
                name=name,
                line=dict(color=color, width=2)
            )
        )
        add_trace(taxes, "Total Tax", "red")
        add_trace(tax_wo_fifth, "Total Tax wo Fifth rule", "orange")
        add_trace(tax_only_sev, "Severance only tax", "blue")
        add_trace(net_incomes, "Net Income", "green")
        add_trace(salaries, "Salary trend", "black" )

        # Update layout
        fig.update_layout(
            title=f"Tax Summary (Year {assessment_year})",
            xaxis_title="Salary (€)",
            yaxis_title="Amount (€)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            template="plotly_white"
        )

        # Show the plot
        fig.show()

    def plot_var_sevpay(start_salary, end_salary, step, start_sev, end_sev, assessment_year, joint_filing, plot_name):
        # Create salary range
        salaries = np.arange(start_salary, end_salary, step)

        sevpays = np.linspace(start_sev, end_sev, 5)

        plotlist = []

        for sevpay in sevpays:
            taxes = []
            tax_wo_fifth = []
            tax_only_sev = []
            net_incomes = []
            for salary in salaries:
                calculator = tc.TaxCalculator(salary=salary, severance_pay=sevpay, assessment_year=assessment_year, joint_filing=joint_filing)
                if plot_name == "total_tax":taxes.append(calculator.get_total_tax())
                elif plot_name == "total_tax_wo_fifth":tax_wo_fifth.append(calculator.get_total_tax_wo_fifth())
                elif plot_name == "tax_sev_only" : tax_only_sev.append(calculator.get_tax_severance_only())
                else: net_incomes.append(calculator.get_net_income())
            
            if plot_name == "total_tax": plot_name == plotlist.append(taxes)
            elif plot_name == "total_tax_wo_fifth":plotlist.append(tax_wo_fifth)
            elif plot_name == "tax_sev_only" :plotlist.append(tax_only_sev)
            else: plotlist.append(net_incomes)

        # Plotly Figure
        fig = go.Figure()

        # Add lines using a helper function
        add_trace = lambda y_values, name: fig.add_trace(
            go.Scatter(
                x=salaries,
                y=y_values,
                mode='lines',
                name=name
            )
        )

        for x in range(5):                                     
            add_trace(plotlist[x], f"{plot_name} with sev pay {sevpays[x]}")

        # Update layout
        fig.update_layout(
            title=f"Tax Summary (Year {assessment_year})",
            xaxis_title="Salary (€)",
            yaxis_title="Amount (€)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            template="plotly_white"
        )

        # Show the plot
        fig.show()

    def plot_netcent_var_sevpay(start_salary, end_salary, step, start_sev, end_sev, assessment_year, joint_filing):
        # Create salary range
        salaries = np.arange(start_salary, end_salary, step)

        sevpays = np.linspace(start_sev, end_sev, 5)

        plotlist = []

        for sevpay in sevpays:
            netcent_incomes = []
            for salary in salaries:
                calculator = tc.TaxCalculator(salary=salary, severance_pay=sevpay, assessment_year=assessment_year, joint_filing=joint_filing)
                netcent_incomes.append(calculator.get_net_percent())
            plotlist.append(netcent_incomes)

        # Plotly Figure
        fig = go.Figure()

        # Add lines using a helper function
        add_trace = lambda y_values, name: fig.add_trace(
            go.Scatter(
                x=salaries,
                y=y_values,
                mode='lines',
                name=name
            )
        )

        for x in range(5):                                     
            add_trace(plotlist[x], f"Plot with sev pay {sevpays[x]}")

        # Update layout
        fig.update_layout(
            title=f"Net percentage income (Year {assessment_year})",
            xaxis_title="Taxable Salary (€)",
            yaxis_title="Income Percentage",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            template="plotly_white"
        )

        # Show the plot
        fig.show()

        
