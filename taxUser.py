import taxPlot as tp

class activatePlots:
    plot_summary = True
    plot_total_tax = False
    plot_total_tax_wo_5th = False
    plot_tax_sev_only = False
    plot_net_ncome = False
    plot_net_percentage_income = True
    joint_filing = True
    start_salary = 0
    end_salary = 200000
    start_sev = 0
    end_sev = 215000


# Plot tax summary
if activatePlots.plot_summary == True:
    tp.TaxPlot.plot_tax_summary(
        start_salary=activatePlots.start_salary,
        end_salary=activatePlots.end_salary,
        step=5000,
        severance_pay=activatePlots.end_sev,
        assessment_year=2024,
        joint_filing = activatePlots.joint_filing
    )

if activatePlots.plot_total_tax == True:   
    tp.TaxPlot.plot_var_sevpay(
        start_salary=activatePlots.start_salary,
        end_salary=activatePlots.end_salary,
        step=5000,
        start_sev = activatePlots.start_sev,
        end_sev=activatePlots.end_sev,
        assessment_year=2024,
        joint_filing = activatePlots.joint_filing,
        plot_name= "total_tax"
    )
if activatePlots.plot_total_tax_wo_5th == True:
    tp.TaxPlot.plot_var_sevpay(
        start_salary=activatePlots.start_salary,
        end_salary=activatePlots.end_salary,
        step=5000,
        start_sev = activatePlots.start_sev,
        end_sev=activatePlots.end_sev,
        assessment_year=2024,
        joint_filing = activatePlots.joint_filing,
        plot_name= "total_tax_wo_fifth"
    )

if activatePlots.plot_tax_sev_only == True:
    tp.TaxPlot.plot_var_sevpay(
        start_salary=activatePlots.start_salary,
        end_salary=activatePlots.end_salary,
        step=5000,
        start_sev = activatePlots.start_sev,
        end_sev=activatePlots.end_sev,
        assessment_year=2024,
        joint_filing = activatePlots.joint_filing,
        plot_name= "tax_sev_only"
    )

if activatePlots.plot_net_ncome == True:
    tp.TaxPlot.plot_var_sevpay(
        start_salary=activatePlots.start_salary,
        end_salary=activatePlots.end_salary,
        step=5000,
        start_sev = activatePlots.start_sev,
        end_sev=activatePlots.end_sev,
        assessment_year=2024,
        joint_filing = activatePlots.joint_filing,
        plot_name= "net_income"
    )

if activatePlots.plot_net_percentage_income == True:
    tp.TaxPlot.plot_netcent_var_sevpay(
        start_salary=activatePlots.start_salary,
        end_salary=activatePlots.end_salary,
        step=5000,
        start_sev = activatePlots.start_sev,
        end_sev=activatePlots.end_sev,
        assessment_year=2024,
        joint_filing = activatePlots.joint_filing
    )



