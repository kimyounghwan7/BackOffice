'use client'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Fragment } from 'react'

export default function dashboard() {
	return (
		<Fragment>
			<div className="flex items-center justify-center min-h-screen bg-gray-100">
				<Card className="w-full max-w-sm">
					<CardHeader>
						<CardTitle className="text-center">대시보드</CardTitle>
					</CardHeader>
					<CardContent>대시보드</CardContent>
				</Card>
			</div>
		</Fragment>
	)
}
