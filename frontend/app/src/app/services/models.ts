export interface ApiResponse<T> {
    count: number
    next: null | string
    previous: null | string
    results: T[]
}

export interface Inspection {
    Company: null | string
    inspectorName: null | string
    issuesCriticalCount: number
    issuesWarningCount: number
    itemsOk: number
    title: string
}