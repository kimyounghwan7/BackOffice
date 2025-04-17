'use client'
import { Fragment } from 'react'
import { DataTable } from '@/components/data-table'
import { Button } from '@/components/ui/button'

export default function ArchiveList() {
	return (
		<Fragment>
			<div className="flex w-full gap-2 px-4 justify-end">
				<Button className="max-w-[8rem] flex-1" variant={'default'}>
					작성하기
				</Button>
			</div>
			<div className="flex w-full flex-1 flex-col gap-2 px-4">
				<DataTable columns={[]} data={[]} />
			</div>
		</Fragment>
	)
}
