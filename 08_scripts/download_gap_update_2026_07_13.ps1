$ErrorActionPreference = 'Continue'
$repo = Split-Path -Parent $PSScriptRoot
$out = Join-Path $repo '09_data_exports\gap_update_2026-07-13'
New-Item -ItemType Directory -Force -Path $out | Out-Null

$items = @(
    @{ File='USDPT_attestation_2026-05-31.pdf'; Url='https://learn.anchorage.com/05.31.26_USDPT_Stablecoin_Attestation_Report_signed.pdf' },
    @{ File='Anchorage_Treasury_comment_GENIUS_2026-06-09.pdf'; Url='https://learn.anchorage.com/Anchorage%20Digital%27s%20Comment%20Letter%20on%20Treasury%27s%20NPRM%20for%20GENIUS%20Act%20-%20June%209%202026.pdf' },
    @{ File='Cambridge_CCAF_transactions_monthly_2026-07-13.json'; Url='https://api.ccaf.io/v1/dmd/transactions?project=dmd&interval=monthly' },
    @{ File='Cambridge_tokenised_money_2026.pdf'; Url='https://www.jbs.cam.ac.uk/wp-content/uploads/2026/02/2026-ccaf-tokenised-money-use-cases-interoperability-and-regulation.pdf' },
    @{ File='USDPT_reserve_attestations_index_2026-07-13.html'; Url='https://www.anchorage.com/platform/usdpt-reserve-attestations-anchorage-digital' },
    @{ File='Taiwan_VASP_passed_bills_2026-07-13.html'; Url='https://lis.ly.gov.tw/lynewbillc/newbillkm' },
    @{ File='Taiwan_VASP_plenary_record_2026-06-30.html'; Url='https://ppg.ly.gov.tw/ppg/sittings/meetingLink?id=11-05-15%3B115%2F06%2F26%3B%E9%99%A2%E6%9C%83' },
    @{ File='Taiwan_VASP_third_reading_summary_2026-07-01.html'; Url='https://www.ly.gov.tw/Pages/Detail.aspx?nodeid=47503&pid=263679' },
    @{ File='Taiwan_Presidential_Gazette_index_2026-07-13.html'; Url='https://www.president.gov.tw/page/129?DeteailNo=4' },
    @{ File='Taiwan_stablecoin_subrules_discussion_2026-07-09.html'; Url='https://www.ly.gov.tw/Pages/Detail.aspx?nodeid=47221&pid=263810' }
)

foreach ($item in $items) {
    $path = Join-Path $out $item.File
    try {
        Invoke-WebRequest -Uri $item.Url -OutFile $path -Headers @{ 'User-Agent'='Mozilla/5.0 RWA-stablecoin-research/1.0' } -MaximumRedirection 8 -TimeoutSec 120
        Write-Host "downloaded $($item.File) $((Get-Item $path).Length) bytes"
    }
    catch {
        Write-Warning "failed $($item.File): $($_.Exception.Message)"
    }
}
