'use client'
import { DataTable } from '@/components/data-table'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Separator } from '@/components/ui/separator'
import { Fragment } from 'react'

export default function Dashboard() {
	return (
		<Fragment>
			<div className="flex w-full flex-1 flex-col items-center justify-center gap-1 px-4">
				<Card className="flex w-full flex-1 flex-col gap-1 py-4">
					<CardHeader className="flex items-center">
						<CardTitle className="w-50 flex-auto text-start">공지사항</CardTitle>
						<Button className="max-w-[8rem] flex-auto" variant={'outline'}>
							바로가기
						</Button>
					</CardHeader>
					<Separator className="mt-2 mb-4" orientation="horizontal" />
					<CardContent>
						<DataTable columns={[]} data={[]} />
					</CardContent>
				</Card>
			</div>
			<div className="flex w-full items-center justify-center gap-2 px-4">
				<Card className="flex-1 gap-1 py-4">
					<CardHeader className="flex items-center">
						<CardTitle className="w-50 flex-auto text-start">자료 수</CardTitle>
						<Button className="max-w-[8rem] flex-auto" variant={'outline'}>
							일반 검색
						</Button>
						<Button className="max-w-[8rem] flex-auto" variant={'outline'}>
							AI 검색
						</Button>
					</CardHeader>
					<Separator className="mt-2 mb-4" orientation="horizontal" />
					<CardContent>
						<h2>5 개</h2>
					</CardContent>
				</Card>
				<Card className="flex-1 gap-1 py-4">
					<CardHeader className="flex items-center">
						<CardTitle className="w-50 flex-auto text-start">결재대기</CardTitle>
						<Button className="max-w-[8rem] flex-auto" variant={'outline'}>
							바로가기
						</Button>
					</CardHeader>
					<Separator className="mt-2 mb-4" orientation="horizontal" />
					<CardContent>
						<h2>5 개</h2>
					</CardContent>
				</Card>
			</div>
			<div className="flex w-full items-center justify-center gap-2 px-4">
				<Card className="flex-1 min-h-[20rem] gap-1 py-4">
					<CardHeader className="flex items-center">
						<CardTitle className="w-50 flex-auto text-start">보고서</CardTitle>
						<Button className="max-w-[8rem] flex-auto" variant={'outline'}>
							바로가기
						</Button>
					</CardHeader>
					<Separator className="mt-2 mb-4" orientation="horizontal" />
					<CardContent>
						<DataTable columns={[]} data={[]} />
					</CardContent>
				</Card>
				<Card className="flex-1 min-h-[20rem] gap-1 py-4">
					<CardHeader className="flex items-center">
						<CardTitle className="w-50 flex-auto text-start">자료실</CardTitle>
						<Button className="max-w-[8rem] flex-auto" variant={'outline'}>
							바로가기
						</Button>
					</CardHeader>
					<Separator className="mt-2 mb-4" orientation="horizontal" />
					<CardContent>
						<DataTable columns={[]} data={[]} />
					</CardContent>
				</Card>
			</div>
		</Fragment>
	)
}
