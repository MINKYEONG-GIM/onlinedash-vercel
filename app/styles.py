DARK_CSS = """<style>
.stApp,.block-container{background:#0f172a}.block-container{padding-top:2.5rem;padding-bottom:2rem}
.fashion-title{display:inline-block;background:#14b8a6;color:#0f172a;padding:0.65rem 1.2rem;border-radius:8px 8px 0 0;font-weight:700;font-size:1.25rem;margin:0.5rem 0 0}
.update-time{font-size:0.85rem;color:#94a3b8;margin-top:0.25rem}
.section-title{font-size:2.2rem;font-weight:700;color:#f1f5f9;margin:1rem 0 0.5rem 0}
.kpi-card-dark{background:#1e293b;color:#f1f5f9;border-radius:10px;padding:1rem 1.2rem;text-align:center;font-weight:600;min-height:100px;display:flex;flex-direction:column;justify-content:center;border:1px solid #334155}
.kpi-card-dark .label{font-size:1.1rem;margin-bottom:0.3rem;color:#cbd5e1}.kpi-card-dark .value{font-size:1rem;font-weight:700;color:#f1f5f9}
.monitor-table{width:100%;border-collapse:collapse;background:#1e293b;color:#f1f5f9}
.monitor-table th,.monitor-table td{border:none;padding:6px 8px;text-align:center;font-size:0.95rem}
.monitor-table thead th{background:#0f172a;color:#f1f5f9;font-weight:700}
.monitor-table thead th.col-emphasis{border:3px solid #fbbf24}
.monitor-table tr.bu-row td{background:#d9f7ee;color:#000;font-size:1.15rem;font-weight:700}
.monitor-table .rate-help,.monitor-table .avg-help,.monitor-table .sum-help{position:relative;display:inline-block;cursor:help}
.monitor-table .rate-help::after,.monitor-table .avg-help::after,.monitor-table .sum-help::after{content:"";position:absolute;opacity:0;pointer-events:none;left:50%;transform:translateX(-50%);bottom:calc(100% + 6px);white-space:pre-line;width:max-content;max-width:360px;background:#ffffff;color:#1e293b;padding:8px 12px;border-radius:6px;font-size:0.85rem;text-align:left;box-shadow:0 4px 12px rgba(0,0,0,0.2);border:1px solid #e2e8f0;z-index:20}
.monitor-table .rate-help:hover::after,.monitor-table .avg-help:hover::after,.monitor-table .sum-help:hover::after{content:attr(data-tooltip);opacity:1}
.monitor-table th.th-sort{white-space:nowrap;cursor:default}.monitor-table th.th-sort .sort-arrow{color:#94a3b8;text-decoration:none;margin-left:4px;font-size:0.75rem;cursor:pointer}.monitor-table th.th-sort .sort-arrow:hover{color:#f1f5f9}
.monitor-table .rate-cell,.monitor-table .avg-cell{display:inline-flex;align-items:center;gap:6px;justify-content:center;position:relative;cursor:help}
.monitor-table .rate-dot{width:16px;height:16px;border-radius:50%;display:inline-block}
.monitor-table .rate-red{background:#ef4444}.monitor-table .rate-yellow{background:#f59e0b}.monitor-table .rate-green{background:#22c55e}
.monitor-table .rate-cell::after,.monitor-table .avg-cell::after{content:"";position:absolute;opacity:0;pointer-events:none;left:50%;transform:translateX(-50%);bottom:calc(100% + 6px);white-space:pre-line;width:max-content;max-width:360px;background:#ffffff;color:#1e293b;padding:8px 12px;border-radius:6px;font-size:0.85rem;box-shadow:0 4px 12px rgba(0,0,0,0.2);border:1px solid #e2e8f0;z-index:20}
.monitor-table .rate-cell:hover::after,.monitor-table .avg-cell:hover::after{content:attr(data-tooltip);opacity:1}
.monitor-table thead th:hover{z-index:10}
.monitor-table .avg-help.tt-left::after{left:0;transform:translateX(0);bottom:calc(100% + 6px)}
.monitor-table td.col-emphasis,.monitor-table th.col-emphasis{font-size:1.045rem;color:#fbbf24}
.monitor-table td.col-small,.monitor-table th.col-small{font-size:0.855rem}
.monitor-table .th-sub{font-size:0.7rem;color:#f1f5f9;font-weight:normal;display:block;margin-top:2px}
.monitor-table{table-layout:fixed}
.monitor-table th.col-small,.monitor-table td.col-small{width:90px;min-width:90px;max-width:90px;box-sizing:border-box}
.monitor-table th.col-emphasis,.monitor-table td.col-emphasis{width:120px;min-width:120px;max-width:120px;box-sizing:border-box}
.monitor-table thead th.col-emphasis{border:3px solid #fbbf24}
.table-wrap.monitor-table-wrap{max-height:500px;overflow-y:auto;overflow-x:auto;border:1px solid #334155;border-radius:8px}
.inout-table{width:100%;border-collapse:collapse;background:#1e293b;color:#f1f5f9;border:1px solid #334155;border-radius:8px;overflow:hidden}
.inout-table th,.inout-table td{border:1px solid #334155;padding:6px 8px;text-align:center;font-size:0.95rem}
.inout-table thead th{background:#0f172a;color:#f1f5f9;font-weight:700}
.inout-table tr.bu-row td{background:#d9f7ee;color:#000;font-size:1.15rem;font-weight:700}.inout-table .brand-cell{text-align:left}
[data-testid='stSelectbox'] label,[data-testid='stMultiSelect'] label{color:#f1f5f9!important}
</style>"""

